#!/usr/bin/python3
"""
gets top 10 posts in a subreddit
"""

import json
import requests


def top_ten(subreddit):
    """
    gets top 10 posts in a subreddit
    """
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'chrome:com.example.myredditapp:v1.2.3 (by /u/oryan)'
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print('None')
        return
    r_json = json.loads(r.text)

    if len(r_json['data']['children']) == 0:
        print('None')
        return

    for post in r_json['data']['children']:
        print(post['data']['title'])
