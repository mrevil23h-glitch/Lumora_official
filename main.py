from telegram.ext import Application, CommandHandler

import bot.config as config
from bot.database import create_database
from bot.admin import admin
from bot.premium import premium
from bot.support import support


async def start(update, context):

    await update.message.reply_text(
        "🌙 Bienvenue sur Lumora"
    )


def main():

    create_database()


    app = Application.builder().token(
        config.BOT_TOKEN
    ).build()


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("premium", premium)
    )

    app.add_handler(
        CommandHandler("support", support)
    )

    app.add_handler(
        CommandHandler("admin", admin)
    )


    print("Lumora lancé")

    app.run_polling()



if __name__ == "__main__":
    main()
