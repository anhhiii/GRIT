import os
import pandas as pd
from database.db import get_connection, create_tables

def seed_books():
    # 1. Tạo bảng nếu chưa có
    create_tables()
    
    # 2. Kiểm tra file CSV
    csv_path = 'data/books.csv'
    if not os.path.exists(csv_path):
        print(f"File {csv_path} không tồn tại!")
        return
    
    # 3. Đọc file CSV
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Lỗi khi đọc file CSV: {e}")
        return
    
    # 4. Kết nối và ghi đè vào SQLite
    conn = get_connection()
    if conn is None:
        return
    try:
        df.to_sql('books', conn, if_exists='replace', index=False)
        print("Đã nạp thành công dữ liệu vào database!")
    except Exception as e:
        print(f"Lỗi khi nạp data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_books()