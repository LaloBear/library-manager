import book
import library_manager

library = library_manager.Library()

book1 = book.Book("The Cat in the Hat", "Dr. Seuss", 1957)
book2 = book.Book("Green Eggs and Ham", "Dr. Seuss", 1960)
book3 = book.Book("The Lorax", "Dr. Seuss", 1971)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.load_books()

while True:
    print("\n Library Menu")
    print("1. Display books")
    print("2. Find book")
    print("3. Check out book")
    print("4. Return book")
    print("5. Remove book")
    print("6. Add book")
    print("7. Display available books")
    print("8. Display checked out books")
    print("9. Find books by author")
    print("10. Display books sorted by title")
    print("11. Exit")
    choice = input("Choose an option:").strip()

    if choice == "1":
        library.display_books()
    
    elif choice == "2":
        title = input("Enter the book title: ")
        library.find_book(title)
    
    elif choice == "3":
        title = input("Enter the book title: ")
        if library.check_out_book(title):
            library.save_books()

    elif choice == "4":
        title = input("Enter the book title: ")
        if library.return_book(title):
            library.save_books()

    elif choice == "5":
        title = input("Enter the book title: ")
        confirmation = input("Are you sure? (yes/no): ").strip().lower()

        if confirmation == "yes":
            if library.remove_book(title):
                print("Book removed.\n")
                library.save_books()
            else:
                print("Book not found.\n")

        elif confirmation == "no":
            print("Book not removed.\n")
        
        else:
            print("Invalid response.\n")

    elif choice == "6":
        title = input("Enter the title: ")
        if title.strip() == "":
            print("Title cannot be empty.\n")
            continue

        author = input("Enter the author: ")
        if author.strip() == "":
            print("Author cannot be empty.\n")
            continue
        try:
            year = int(input("Enter year published: "))
        except ValueError:
            print("Invalid response.")
            continue
        
        new_book = book.Book(title, author, year)
        if library.add_book(new_book):
            print(f"{title} was added.\n")
            library.save_books()
        else:
            print("This book already exists.\n")
    
    elif choice == "7":
        library.display_available_books()

    elif choice == "8":
        library.display_checked_out_books()

    elif choice == "9":
        author = input("Enter author:")

        library.find_books_by_author(author)

    elif choice == "10":
        library.display_books_sorted_by_title()

    elif choice == "11":
        library.save_books()
        print("Goodbye!")

        break

    else:
        print("Invalid choice. Try again")