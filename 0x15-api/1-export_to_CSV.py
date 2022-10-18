#!/usr/bin/python3
"""
Gets employees Todos fro an API
"""


if __name__ == '__main__':
    import csv
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    completed = []
    total = []

    res1 = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                        .format(user_id)).text

    username = json.loads(res1)[0].get('name')

    res2 = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).text
    todos = json.loads(res2)

    with open('{}.csv'.format(user_id), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for todo in todos:
            line = ['{}'.format(user_id), '{}'.format(username),
                    '{}'.format(todo.get('completed')),
                    '{}'.format(todo.get('title'))]
            print(line)
            writer.writerow(line)
