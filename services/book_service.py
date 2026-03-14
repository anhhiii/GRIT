from models.book import Book

class BookService:
    @staticmethod
    def get_books():
        """
        Lấy danh sách tất cả các sách.
        """
        books = Book.get_all()
        # Có thể thêm logic xử lý dữ liệu ở đây (nếu cần)
        return books

    @staticmethod
    def get_book_details(book_id):
        """
        Lấy thông tin chi tiết của một cuốn sách dựa trên ID.
        """
        book = Book.get_by_id(book_id)
        # Có thể thêm logic xử lý dữ liệu ở đây (nếu cần)
        return book

    @staticmethod
    def search_books(keyword):
        """
        Tìm kiếm sách theo tiêu đề hoặc tác giả.
        """
        books = Book.get_all()
        if books.empty:
            return books
        # Lọc sách theo từ khóa
        filtered_books = books[
            books['title'].str.contains(keyword, case=False, na=False) |
            books['author'].str.contains(keyword, case=False, na=False)
        ]
        return filtered_books