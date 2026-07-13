#!/usr/bin/python3
"""Module that recursively counts keyword occurrences in hot post titles."""
import requests


def count_words(
        subreddit, word_list, instances=None, word_freq=None,
        after="", first_call=True):
    """Recursively count occurrences of given keywords in hot post titles.

    Prints results sorted by count (descending), then alphabetically.
    Prints nothing if the subreddit is invalid or no matches are found.
    Duplicate keywords in word_list have their counts summed together.
    """
    if first_call:
        lowered = [word.lower() for word in word_list]
        word_freq = {}
        for word in lowered:
            word_freq[word] = word_freq.get(word, 0) + 1
        instances = {word: 0 for word in word_freq}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data")
    posts = data.get("children")

    for post in posts:
        title = post.get("data").get("title").lower()
        for token in title.split():
            if token in instances:
                instances[token] += 1

    next_after = data.get("after")
    if next_after:
        return count_words(
            subreddit, word_list, instances, word_freq, next_after, False
        )

    totals = {}
    for word, count in instances.items():
        total = count * word_freq[word]
        if total > 0:
            totals[word] = total

    if not totals:
        return

    sorted_results = sorted(totals.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_results:
        print("{}: {}".format(word, count))
