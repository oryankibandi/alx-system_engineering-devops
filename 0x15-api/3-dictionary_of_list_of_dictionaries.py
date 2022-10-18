#!/usr/bin/python3
"""
Gets employees Todos fro an API
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_data = {}
    temp_data = {}
    temp_username = ''

    res1 = requests.get('https://jsonplaceholder.typicode.com/users').text

    users = json.loads(res1)
    for user in users:
        temp_username = user.get('username')
        temp_id = user.get('id')
        res2 = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(temp_id)).text
        user_data['{}'.format(temp_id)] = []
        todos = json.loads(res2)
        for todo in todos:
            temp_data['username'] = temp_username
            temp_data['task'] = todo.get('title')
            temp_data['completed'] = todo.get('completed')

            user_data['{}'.format(temp_id)].append(temp_data)

    user_data_string = json.dumps(user_data)

    with open('todo_all_employees.json', 'w') as f:
        f.write(user_data_string)
