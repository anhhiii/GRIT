import os
import requests
import json
from dotenv import load_dotenv
from database.db import get_connection

# ===== LOAD ENV =====
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ===== MAP CATEGORY =====
category_map = {
    1: "Văn học",
    2: "Kinh tế",
    3: "Kỹ năng",
    4: "Lịch sử",
    5: "tâm lý",
    6: "khoa học",
    7: "trinh thám",
    8: "novel",
    9: "fiction",
    10: "finance",
    11: "history",
    12: "science",
    13: "mystery",
    14: "nấu ăn",
    15: "biện chứng",
    16: "startup",
    17: "marketing",
    18: "lead",
    20: "kiếm hiệp",
    21: "tiểu thuyết",
    22: "bi kịch",
    23: "hài kịch",
    24: "physics",
    25: "biology"
}

# ===== LẤY DATA =====
def get_books_from_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, category_id FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

# ===== FORMAT DATA =====
def format_books(books):
    formatted = []

    for title, author, category_id in books:
        genre = category_map.get(category_id, "Khác")
        formatted.append(f"{title} - {author} ({genre})")

    return "\n".join(formatted)

# ===== BUILD PROMPT =====
def build_prompt(user_input, books):
    return f"""
Bạn là chatbot tư vấn sách cho website Hiên Chữ.

CHỈ được phép đề xuất sách từ danh sách bên dưới.
Không được bịa thêm sách ngoài danh sách.

DANH SÁCH SÁCH:
{books}

NHIỆM VỤ:
- Hiểu nhu cầu người dùng (thể loại, cảm xúc, mục đích đọc)
- Chọn ra 3-5 cuốn phù hợp nhất
- Ưu tiên đúng thể loại

Nếu không có sách phù hợp:
→ nói rõ và gợi ý gần nhất

FORMAT TRẢ LỜI:
- Tên sách (tác giả): lý do

User: {user_input}
"""

def chat_with_recommendation(user_input):
    if not GROQ_API_KEY:
        return "Lỗi hệ thống: Chưa cấu hình GROQ_API_KEY trong file .env"

    try:
        books = get_books_from_db()
        books = books[:30]
        book_text = format_books(books)

        prompt = build_prompt(user_input, book_text)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "Bạn là chuyên gia về sách của hệ thống Hiên Chữ."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"Lỗi từ Groq API: {response.status_code} - {response.text}"

    except Exception as e:
        return f" Lỗi hệ thống: {str(e)}"