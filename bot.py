
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


# Informations d'authentification Telegram
telegram_token = '6445094207:AAE5AqlctyhsBUiQ0OMuM0mv0R4BfEl0TF8'

# Informations d'authentification
api_key = '447088687629111c58c3573.70152188'
api_secret = '415625848629a242b4b94d1.61917217'

# Création d'un bot Telegram
bot = telegram.Bot(token=telegram_token)

# Fonction pour gérer la commande /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bienvenue ! Utilisez /pay pour initier un paiement.")

# Fonction pour gérer la commande /pay
def pay(update: Update, context: CallbackContext) -> None:
    amount = 1000  # Montant en centimes
    transaction_id = 'REF12345'  # Référence unique pour la transaction

    payment_url = f"https://api.cinetpay.com/v1/payment/{api_key}/{transaction_id}/{amount}"
    update.message.reply_text(f"Cliquez sur le lien pour effectuer le paiement : {payment_url}")

def main():
    updater = Updater(token=telegram_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("pay", pay))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()