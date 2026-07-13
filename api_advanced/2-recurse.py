#!/usr/bin/python3
"""Module that recursively queries the Reddit API for hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after="", first_call=True):
    """Return a list of titles of all hot articles for a subreddit.

    Uses recursion and pagination to traverse every page of results.
    If the subreddit is invalid, return None.
    """
    if first_call:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None if first_call else hot_list

    data = response.json().get("data")
    posts = data.get("children")

    if not posts and first_call:
        return None

    for post in posts:
        hot_list.append(post.get("data").get("title"))

    next_after = data.get("after")
    if next_after is None:
        return hot_list

    return recurse(subreddit, hot_list, next_after, False)
