import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def handle_message(update, context):
    # Lógica para responder às mensagens recebidas
    pass


def handle_command(update, context):
    # Lógica para responder aos comandos recebidos
    pass

def start_bot():
    # Criação do objeto Updater e passagem do token de acesso
    updater = Updater(token='6406389382:AAEAk8-xln_KfRnUvAit7AfxfzsHJ5QcX0I', use_context=True)

    # Configuração dos handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", handle_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    # Inicia o bot
    updater.start_polling()
    updater.idle()