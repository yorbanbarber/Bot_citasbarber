from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

   # Token de tu bot (obtenido de BotFather)
   TOKEN = "7524999845:AAG9hPdc3Mnu42IpdgDk4NMFUqCJxtZA4lo"

   # Comando /start
   def start(update, context):
       update.message.reply_text("¡Hola! Soy tu gestor de citas. Usa /agendar para programar una cita.")

   # Comando /agendar
   def agendar(update, context):
       update.message.reply_text("Por favor, escribe la fecha y hora de tu cita (por ejemplo: 27/02/2025 15:00).")

   # Manejar mensajes de texto
   def manejar_mensaje(update, context):
       texto = update.message.text
       update.message.reply_text(f"Cita agendada: {texto}. ¡Gracias!")

   # Iniciar el bot
   def main():
       updater = Updater(TOKEN, use_context=True)
       dp = updater.dispatcher

       # Manejadores de comandos
       dp.add_handler(CommandHandler("start", start))
       dp.add_handler(CommandHandler("agendar", agendar))

       # Manejador de mensajes de texto
       dp.add_handler(MessageHandler(Filters.text & ~Filters.command, manejar_mensaje))

       # Iniciar el bot
       updater.start_polling()
       updater.idle()

   if __name__ == "__main__":
       main()