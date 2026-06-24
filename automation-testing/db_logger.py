import sqlite3
from datetime import datetime

DB_PATH = "test_results.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name   TEXT,
            status      TEXT,
            duration    REAL,
            error_msg   TEXT,
            run_at      TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_result(test_name, status, duration, error_msg=None):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO test_results (test_name, status, duration, error_msg, run_at)
        VALUES (?, ?, ?, ?, ?)
    """, (test_name, status, duration, error_msg, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()