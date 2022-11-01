#!/usr/bin/python3
"""
gets hot posts in a subreddit recursively
"""


import json
import requests


def count_words(subreddit, word_list, word_dict=None, url=None):
    """
    gets hot posts in a subreddit recursively
    """
    if url is None:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=200'.format(
            subreddit)

    if word_dict is None:
        word_dict = {}
        for word in word_list:
            word_dict[word] = 0

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
        w_split = post['data']['title'].split(' ')
        for w in w_split:
            if w.lower() in list(word_dict.keys()):
                word_dict[w.lower()] += 1

    if r_json['data']['after'] is None:
        word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        word_dict = dict(word_dict)
        for k, v in word_dict.items():
            print('{}: {}'.format(k, v))
        return word_dict
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=200&after={}'.format(
            subreddit, r_json['data']['after'])
        return count_words(subreddit, word_list, word_dict, url)
