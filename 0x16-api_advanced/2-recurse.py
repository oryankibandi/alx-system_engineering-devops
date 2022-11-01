#!/usr/bin/python3
"""
gets hot posts in a subreddit recursively
"""

import json
import requests


def recurse(subreddit, hot_list=[], url=None):
    """
    gets hot posts in a subreddit recursively
    """
    if url is None:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=200'.format(
            subreddit)

    headers = {
        'User-Agent': 'chrome:com.example.myredditapp:v1.2.3 (by /u/oryan)'
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return None
    r_json = json.loads(r.text)

    if len(r_json['data']['children']) == 0:
        return None

    for post in r_json['data']['children']:
        hot_list.append(post['data']['title'])

    if r_json['data']['after'] is None:
        return hot_list
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=200&after={}'.format(
            subreddit, r_json['data']['after'])
        return recurse(subreddit, hot_list, url)
