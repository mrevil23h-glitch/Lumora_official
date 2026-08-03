from telegram import Update
from telegram.ext import ContextTypes

import bot.config as config


async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
f"""
⭐ LUMORA PREMIUM

Prix : {config.PREMIUM_PRICE}

Crypto :
{config.CRYPTO_ADDRESS}

Support :
{config.SUPPORT_ADDRESS}
"""
    )
