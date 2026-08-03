import sqlite3


DATABASE = "../database/lumora.db"


def connect():

    return sqlite3.connect(
        DATABASE
    )


def create_users():

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS website_users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)


    db.commit()
    db.close()
