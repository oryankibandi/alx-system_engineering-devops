#!/usr/bin/python3
"""
Gets employees Todos fro an API
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user_data = {
        "{}".format(user_id): []
    }
    temp_data = {}

    res1 = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                        .format(user_id)).text

    username = json.loads(res1)[0].get('name')

    res2 = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user_id)).text
    todos = json.loads(res2)

    for todo in todos:
        temp_data['task'] = todo.get('title')
        temp_data['completed'] = todo.get('completed')
        temp_data['username'] = username
        user_data['{}'.format(user_id)].append(temp_data)

    user_data_string = json.dumps(user_data)

    with open('{}.json'.format(user_id), 'w') as f:
        f.write(user_data_string)
