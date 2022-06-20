import os, json, time, requests
from requests.exceptions import Timeout

os.system('title Website Monitoring')
with open('webhook.txt', 'r') as f:
    webhook = f.read()
target = input('Ссылка на сайт: ')
timeout = input('Время ожидания (В секундах): ')
delay = input('Задержка: ')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = f'{webhook}'
data = {"content": "@everyone","embeds": [{"title": "Website Monitoring","description": f"Я заметил, что {target} стал недоступным.","color": 45055}],"username": "Monitoring","avatar_url": "https://cdn.discordapp.com/attachments/976964439561633872/988547327268651018/avatar.png","attachments": []}


while True:
 time.sleep(float(delay))
 try:
     r = requests.get(target, timeout, headers=headers)
     if r.status_code != 200:
         requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
 except Timeout:
     requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})