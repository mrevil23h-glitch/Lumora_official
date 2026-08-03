import bot.config as config


def check_admin(user_id):

    if user_id == config.ADMIN_ID:

        return True

    return False



def admin_message():

    return """
👑 Lumora Admin

Gestion utilisateurs
Gestion Premium
Gestion paiements
"""
