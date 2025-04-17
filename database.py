import sqlite3

DB_NAME = "guests.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                item TEXT NOT NULL
            )
        """)
        conn.commit()

def get_guests():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT name, item FROM guests")
        return c.fetchall()

def add_guest(name, item):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO guests (name, item) VALUES (?, ?)", (name, item))
        conn.commit()

def item_exists(item):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT 1 FROM guests WHERE LOWER(item) = LOWER(?)", (item,))
        return c.fetchone() is not None