\# ALU Scripting: Reddit API - Advanced



This project contains a set of Python scripts that query the

Reddit API to retrieve subreddit information, hot posts, and

keyword statistics.



\## Files



| File | Description |

| --- | --- |

| `0-subs.py` | `number\_of\_subscribers(subreddit)` — returns the subscriber count for a subreddit, or `0` if invalid. |

| `1-top\_ten.py` | `top\_ten(subreddit)` — prints the titles of the first 10 hot posts, or `None` if invalid. |

| `2-recurse.py` | `recurse(subreddit, hot\_list=\[])` — recursively paginates through every hot post and returns a list of all titles, or `None` if invalid. |

| `3-count.py` | `count\_words(subreddit, word\_list)` — recursively counts keyword occurrences in hot post titles, printed sorted by count then alphabetically. |



\## Requirements



\- Python 3, `requests` module

\- Custom `User-Agent` header on every request

\- `allow\_redirects=False` to detect invalid subreddits correctly



\## Author



Written as part of the ALU Back-End Web Development curriculum.

