import sqlite3


DATABASE = "database/lumora.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_database():

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        premium INTEGER DEFAULT 0
    )
    """)

    db.commit()
    db.close()


def add_user(user_id, username):

    db = connect()
    cursor = db.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users(id,username) VALUES(?,?)",
        (user_id, username)
    )

    db.commit()
    db.close()
