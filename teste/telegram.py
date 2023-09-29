import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
  
   
api_id = 'API_id'
api_hash = 'API_hash'
token = '6406389382:AAEAk8-xln_KfRnUvAit7AfxfzsHJ5QcX0I'
phone = '+5561981259018'
   
client = TelegramClient('session', api_id, api_hash) 
   
client.connect() 
  
if not client.is_user_authorized(): 
   
    client.send_code_request(phone) 
      
    client.sign_in(phone, input('Enter the code: ')) 
   
try: 
    receiver = InputPeerUser('user_id', 'user_hash') 
    client.send_message(receiver, "Ocorreu um erro na sua automação", parse_mode='html') 

except Exception as e: 
    print(e); 


client.disconnect() 