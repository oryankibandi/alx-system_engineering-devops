#!/usr/bin/python3
"""
Gets employees Todos fro an API
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    completed = []
    total = []

    res1 = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'
        .format(user_id)).text

    username = json.loads(res1)[0].get('name')

    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user_id)).text
    todos = json.loads(res2)

    for todo in todos:
        if todo.get('completed'):
            completed.append(todo)

    print("Employee {} is done with tasks({}/{}):"
          .format(username, len(completed), len(todos)))
    for item in completed:
        print('\t{}'.format(item.get('title')))
