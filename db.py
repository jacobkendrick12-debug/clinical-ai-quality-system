import sqlite3

conn = sqlite3.connect("clinical.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS consultations (
    id INTEGER PRIMARY KEY,
    status TEXT,
    transcript TEXT,
    clinical_data TEXT,
    reasons TEXT
)
""")

conn.commit()