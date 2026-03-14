import sqlite3

def get_connection():
    try:
        conn = sqlite3.connect('database/grit_books.db')
        return conn
    except sqlite3.Error as e:
        print(f"Lỗi kết nối database: {e}")
        return None

def create_tables():
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT,
                category_id INTEGER,
                description TEXT,
                img_url TEXT,
                isbn TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Lỗi khi tạo bảng: {e}")
    finally:
        conn.close()