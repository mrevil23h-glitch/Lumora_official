import hashlib


def encrypt_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def check_password(password, saved):

    return encrypt_password(password) == saved
