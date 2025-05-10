import sqlite3

conn = sqlite3.connect('student.db')
c = conn.cursor()

# Table for users (login)
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Table for students
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert admin user (run only once)
c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', 'password'))

conn.commit()
conn.close()
