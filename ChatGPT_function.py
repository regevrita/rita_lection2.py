import os

import requests



#
# URL = 'https://data.fixer.io/api/convert'
#
#
# response = requests.get(URL, params=
#     {
#     "access_key": 52.52,
#     "from": ,
#     'to': }).json()
#
# print(response['current_weather']['windspeed'])


URL = 'https://api.openai.com/v1/chat/completions'


def ChatGPT(text, token):
    response = requests.post(URL, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',

        }, json={
        "model": "gpt-3.5-turbo",
        "messages": [{'role': 'user', 'content': f'{text}'}]
   })


    return response.json()['choices'][0]['message']['content']

