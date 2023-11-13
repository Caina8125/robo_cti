import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Configure o token do seu bot aqui
tokenn = "6958350096:AAHxsXXkiOjPrLMe0NRllYUGmkdDSzRJjh8"

# Configurar o logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Criar o objeto Updater
updater = Updater(bot="CensoCtiBot", update_queue=tokenn)
# dispatcher = updater.dispatcher


# Função para o comando /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Olá, {user.mention_markdown_v2()}!',
        reply_markup=None
    )

# Função para lidar com mensagens de texto
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

# Adicione comandos e manipuladores
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()

