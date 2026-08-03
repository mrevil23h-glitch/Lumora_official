from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def buttons():

    keyboard = [
        [
            InlineKeyboardButton(
                "⭐ Premium",
                callback_data="premium"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 Support",
                callback_data="support"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
