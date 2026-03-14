import requests
import pandas as pd
import time

def crawl_1000_books():
    target_count = 1000
    books = []
    # Danh sách các từ khóa đa dạng để quét được nhiều sách khác nhau
    keywords = [
        'văn học', 'kinh tế', 'tâm lý', 'lịch sử', 'khoa học', 'trinh thám', 
        'novel', 'fiction', 'finance', 'history', 'science', 'mystery',
        'nấu ăn', 'biện chứng', 'startup', 'marketing', 'leadership',
        'ngôn tình', 'kiếm hiệp', 'tiểu thuyết', 'bi kịch', 'hài kịch',
        'physics', 'biology', 'philosophy', 'religion', 'art', 'music',
        'education', 'health', 'fitness', 'travel', 'cooking', 'hacker',
        'manga', 'thế chiến', 'vũ trụ', 'ai', 'blockchain', 'psychology'
    ]
    
    current_keyword_index = 0
    start_index = 0
    
    print(f"Đang bắt đầu quét dữ liệu... Mục tiêu: {target_count} cuốn.")

    while len(books) < target_count:
        kw = keywords[current_keyword_index]
        # Gọi API với phân trang (startIndex)
        url = f"https://www.googleapis.com/books/v1/volumes?q={kw}&startIndex={start_index}&maxResults=40"
        
        try:
            response = requests.get(url)
            if response.status_code != 200:
                break
                
            items = response.json().get('items', [])
            
            # Nếu hết sách cho từ khóa này, chuyển sang từ khóa tiếp theo
            if not items:
                current_keyword_index += 1
                start_index = 0
                if current_keyword_index >= len(keywords):
                    break
                continue

            for item in items:
                info = item.get('volumeInfo', {})
                
                # BỘ LỌC QUAN TRỌNG: Chỉ lấy nếu có đủ Ảnh và Mô tả
                img = info.get('imageLinks', {}).get('thumbnail')
                desc = info.get('description')
                
                if img and desc: # Nếu cả 2 đều tồn tại (không None)
                    # Chuẩn hóa link ảnh sang https
                    img = img.replace("http://", "https://")
                    
                    book_data = {
                        'title': info.get('title'),
                        'author': ", ".join(info.get('authors', ['Unknown'])),
                        'category_id': current_keyword_index + 1,
                        'description': desc,
                        'img_url': img,
                        'isbn': info.get('industryIdentifiers', [{}])[0].get('identifier', 'N/A')
                    }
                    books.append(book_data)
                    
                    # Dừng lại khi đủ 1000 cuốn
                    if len(books) >= target_count:
                        break
            
            print(f"Đã lấy được: {len(books)} cuốn (Từ khóa: {kw})")
            start_index += 40
            time.sleep(1) # Nghỉ một chút để không bị Google chặn

        except Exception as e:
            print(f"Lỗi: {e}")
            break

    # Lưu thành file
    df = pd.DataFrame(books)
    df.insert(0, 'id', range(1, len(df) + 1))
    df.to_csv('books.csv', index=False, encoding='utf-8-sig')
    print("--- HOÀN THÀNH ---")

crawl_1000_books()