import pandas as pd
from database.db import get_connection

class Book:
    @staticmethod
    def get_all():
        """
        Lấy danh sách tất cả các sách từ cơ sở dữ liệu.
        """
        conn = get_connection()
        if conn is None:
            return pd.DataFrame()
        try:
            query = "SELECT * FROM books"
            df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            print(f"Lỗi khi truy vấn tất cả sách: {e}")
            return pd.DataFrame()
        finally:
            conn.close()

    @staticmethod
    def get_by_id(book_id):
        """
        Lấy thông tin chi tiết của một cuốn sách dựa trên ID.
        """
        conn = get_connection()
        if conn is None:
            return None
        try:
            query = "SELECT * FROM books WHERE id = ?"
            df = pd.read_sql(query, conn, params=(book_id,))
            return df.iloc[0] if not df.empty else None
        except Exception as e:
            print(f"Lỗi khi truy vấn sách với ID {book_id}: {e}")
            return None
        finally:
            conn.close()