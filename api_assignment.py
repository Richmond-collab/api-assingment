"""
Assignment: HTTP, REST APIs & Python Requests
API: https://jsonplaceholder.typicode.com
Install requests first if needed:  pip install requests
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def task1_fetch_post():
    print("=== Task 1: Fetch Data ===")
    try:
        response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
        response.raise_for_status()
        post = response.json()
        print("Title:", post["title"])
        print("Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Task 1 failed:", e)


def task2_filter_posts():
    print("\n=== Task 2: Filter Data ===")
    try:
        response = requests.get(
            f"{BASE_URL}/posts", params={"userId": 1}, timeout=10
        )
        response.raise_for_status()
        posts = response.json()
        print("Total posts for user 1:", len(posts))
    except requests.exceptions.RequestException as e:
        print("Task 2 failed:", e)


def task3_create_post():
    print("\n=== Task 3: Create Data ===")
    new_post = {
        "title": "My Sample Post",
        "body": "This is the body of my sample post created with Python.",
        "userId": 1,
    }
    try:
        response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=10)
        response.raise_for_status()
        print("Status code:", response.status_code)
        print("Response body:", response.json())
    except requests.exceptions.RequestException as e:
        print("Task 3 failed:", e)


if __name__ == "__main__":
    task1_fetch_post()
    task2_filter_posts()
    task3_create_post()