import json 
import book

class Library:
    def __init__(self):
        self.books = []

    def save_books(self):
        books_data = []

        for b in self.books:
            book_data = {
            "title": b.title,
             "author": b.author,
             "year_published": b.year_published,
             "checked_out": b.checked_out
            }

            books_data.append(book_data)

        with open("books.json", "w") as file:
            json.dump(books_data, file)

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                books_data = json.load(file)
        except FileNotFoundError:
            return
        
        self.books = []
        
        for book_data in books_data:
            new_book = book.Book(
                book_data["title"],
                book_data["author"],
                book_data["year_published"]
            )

            new_book.checked_out = book_data["checked_out"]
            self.books.append(new_book)

    def add_book(self, book):
        for b in self.books:
            if book.title.strip().lower() == b.title.strip().lower():
                return False

        self.books.append(book)
        return True 
    
    def display_books(self):
        for b in self.books:
            print(b)

    def find_book(self, title):
        for b in self.books:
            if title.strip().lower() == b.title.strip().lower():
                print(b)
                return
            
        print("Book not found.\n")

    def check_out_book(self, title):
        for b in self.books:
            if title.strip().lower() == b.title.strip().lower():
                if b.checked_out:
                    print("This book is already checked out.\n")
                    return False
                
                b.check_out()
                print("Book checked out.\n")
                return True
                
        print("Book not found.\n")
        return False

    def return_book(self, title):
        for b in self.books:
            if title.strip().lower() == b.title.strip().lower():
                if not b.checked_out:
                    print("This book is not currently checked out.\n")
                    return False
                 
                b.return_book()
                print("Book returned.\n")
                return True
            
        print("Book not found.\n")
        return False

    def remove_book(self, title):
        for b in self.books:
            if title.strip().lower() == b.title.strip().lower():
                self.books.remove(b)
                return True
            
        return False
    
    def display_available_books(self):
        found = False

        for b in self.books:
            if not b.checked_out:
                print(b)
                found = True
            
        if not found:
            print("There are no books available.\n")

    def display_checked_out_books(self):
        found = False

        for b in self.books:
            if b.checked_out:
                print(b)
                found = True
        
        if not found:
            print("There are no books checked out.\n")
    
    def find_books_by_author(self, author):
        found = False

        for b in self.books:
            if b.author.lower().strip() == author.lower().strip():
                found = True
                print(b)

        if not found:
            print("No books found by that author.")

    def display_books_sorted_by_title(self):
        sorted_books = sorted(self.books, key=lambda b: b.title.lower())

        for b in sorted_books:
            print(b)