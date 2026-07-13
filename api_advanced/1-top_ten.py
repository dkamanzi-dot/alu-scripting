#!/usr/bin/python3
"""Module that queries the Reddit API for the top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data").get("children")
    except (AttributeError, ValueError):
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data").get("title"))
