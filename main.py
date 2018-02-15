from settings import token
from time import sleep
import requests

url = "https://api.telegram.org/bot" + token


def get_bot_updates():
    result = requests.get(url +'getUpdates' )
    pydict = result.json()
    return pydict['result']

def send_mess(chat, text):
    params = {'chat_id':chat,'text':text}
    response=requests.post(url + 'sendMessage',data=params)
    return response

res = get_bot_updates()

if len(res)!=0:
    for s in range(len(res)):
        chat=res[s]['message']['from']['id']
        print ('Text:', res[s]['message']['text'])
        print('ID:',res[s]['message']['from']['id'])
        print ('message:', send_mess(chat, 'ну вот'))
print("Это всё что было")