import telegram
import asyncio
import socks
import requests
from telegram.ext import Updater

async def Amhp(aviso):

    # Defina o ID do chat onde as mensagens serão enviadas
    id_amhp = '-357797147'

    my_id = '1148462305'

    

    # Crie um objeto Bot com o token do bot
    myToken = '6958350096:AAHxsXXkiOjPrLMe0NRllYUGmkdDSzRJjh8'
    bot     = telegram.Bot(token=myToken)
    await bot.send_message(chat_id=id_amhp, text=aviso)

# async def Dev(aviso):

async def send_message_with_proxy():
    my_id          = '1148462305'
    proxy_host     = '10.0.0.230'
    proxy_port     = '3128'
    proxy_user     = "lucas.timoteo"
    proxy_pass     = "Caina8125"
    myToken        = '6958350096:AAHxsXXkiOjPrLMe0NRllYUGmkdDSzRJjh8'
    bot            = telegram.Bot(token=myToken)

    proxy_settings = {
    'address': proxy_host,
    'port': proxy_port,
    'username': proxy_user,
    'password': proxy_pass,
    'rdns': True
}
    proxy = socks.socksocket()
    proxy.setproxy(**proxy_settings)
    
    bot._validate_token()
    bot._replace()
    bot._connect()

    # await Updater(token=myToken, use_context=True, request_context=request_context)
    await bot.send_message(chat_id=my_id, text="teste")

# asyncio.run(send_message_with_proxy()) 