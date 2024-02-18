
class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(',')
            print("Book Name:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()

    def add_book(self, title, author, release_date, num_pages):
        self.file.write(f"{title},{author},{release_date},{num_pages}\n")

    def remove_book(self, title):
        self.file.seek(0)  
        books = self.file.readlines()
        self.file.seek(0) 
        for book in books:
            if title not in book:
                self.file.write(book)
        self.file.truncate()  
    def list_books(self):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(',')
            print("Book Name:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()

    def add_book(self, title, author, release_date, num_pages):
        self.file.write(f"{title},{author},{release_date},{num_pages}\n")

    def remove_book(self, title):
        self.file.seek(0)  
        books = self.file.readlines()
        self.file.seek(0)  
        for book in books:
            if title not in book:
                self.file.write(book)
        self.file.truncate()  

lib = Library()
print("*** MENU ***")
print("1) List Books")
print("2) Add Book")
print("3) Remove Book")

choice = input("Enter your choice: ")

if choice == "1":
    lib.list_books()
elif choice == "2":
    title_name = input("Enter book title: ")
    author_name = input("Enter book author: ")
    releasing_date = input("Enter release date: ")
    num_pages = input("Enter number of pages: ")
    lib.add_book(title_name, author_name, releasing_date, num_pages)
elif choice == "3":
    title = input("Enter title of the book to remove: ")
    lib.remove_book(title)
else:
    print("Invalid choice.")

