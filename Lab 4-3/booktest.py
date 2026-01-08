from P1 import Book, TextBook, Magazine

# Create objects
book = Book("Harry Potter", "B001", "J.K. Rowling")
book.set_pages_count(350)

textbook = TextBook("Physics", "T101", "Serway", "Science", 12)
textbook.set_pages_count(500)

magazine = Magazine("Time", "M202", 45)

# Check out some items
book.check_out()
textbook.check_out()

# Display info
print("Book Info:")
book.display_info()
print()

print("TextBook Info:")
textbook.display_info()
print()

print("Magazine Info:")
magazine.display_info()