from telegram import Update
from telegram.ext import ContextTypes

import bot.config as config


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != config.ADMIN_ID:

        await update.message.reply_text(
            "⛔ Accès refusé"
        )
        return


    await update.message.reply_text(
        "👑 Panel Admin Lumora activé"
    )
