from settings import token
import datetime
import requests

url = "https://api.telegram.org/bot" + token

bit_url ="https://api.cryptonator.com/api/ticker/"

def get_updates(offset=0, timeout=30):
    params = {'timeout': timeout, 'offset': offset}
    results = requests.get(url +'getUpdates',data=params )
    pydict = results.json()
    return pydict['result']

def send_message(chat, text):
    params = {'chat_id':chat,'text':text}
    response=requests.post(url + 'sendMessage',data=params)
    return response

def get_price(pair):
    response=requests.get(bit_url+pair)
    data=response.json()['ticker']['price']
    return data

greetings = ('здравствуй', 'привет', 'ку', 'здорово','/start') 

def main():
    offset=None
    newoffset=None
    while True:
        results=get_updates(newoffset)
        for result in results:
            chat_id = result['message']['chat']['id']
            first_name = result['message']['chat']['first_name']
            message_text = result['message']['text']
                
            if message_text.lower() in greetings:
                text1='Привет {},я умею показывать текущий курс биткоина или эфириума'.format(first_name)
                text2='Хочешь узнать курс биткоина отправь /btc'
                text3='Хочешь узнать курс эфириума отправь /eth'
                send_message(chat_id, text1)
                send_message(chat_id, text2)
                send_message(chat_id, text3)
            elif message_text=='/btc':
                text="Bitcoin стоит {} $". format (get_price("/btc-usd"))
                send_message(chat_id,text)
            elif message_text=='/eth':
                text="Etherium стоит {} $". format (get_price("/eth-usd"))
                send_message(chat_id,text)
            else:
                send_message(chat_id,'Не верная команда пришли /start')
            offset=get_updates()
            newoffset=offset[-1]['update_id']+1
if __name__ == '__main__':  
    main()
