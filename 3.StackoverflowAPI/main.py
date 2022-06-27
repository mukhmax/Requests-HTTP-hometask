import time

import requests
import datetime
from pprint import pprint

current_time = datetime.datetime.now()
url = 'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': int(current_time.timestamp()-86400 * 2),
          'todate': int(current_time.timestamp()),
          'tagged': 'python',
          'site': 'stackoverflow',
          'order': 'desc',
          'sort': 'activity',
          'page': 1,
          'pagesize': 100}
questions = []


def questions_get():
    res = requests.get(url, params=params)
    return res.json()


while True:
    dict_page = questions_get()
    for item in dict_page['items']:
        questions.append(item['title'])
    if dict_page['has_more']:
        params['page'] += 1
        time.sleep(0.34)
    else:
        break

pprint(questions)
print(len(questions))
