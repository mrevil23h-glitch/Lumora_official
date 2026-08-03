from telegram import Update
from telegram.ext import ContextTypes

import bot.config as config


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "💬 Support :\n"
        + config.SUPPORT_ADDRESS
    )
