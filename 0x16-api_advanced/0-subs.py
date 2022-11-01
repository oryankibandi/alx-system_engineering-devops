#!/usr/bin/python3
"""Gets the total subs on a subreddit"""

import json
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers on a subreddit"""

    if subreddit is None:
        return (0)

    headers = {
        'User-Agent': 'chrome:com.example.myredditapp:v1.2.3 (by /u/oryan)'
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return 0

    json_r = json.loads(r.text)

    if json_r['data']['subscribers'] is None:
        return 0
    else:
        return json_r['data']['subscribers']
