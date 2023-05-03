import datetime
from prettytable import PrettyTable

def create_book(book_id, title, author, publication_year, publisher, stock):
    books[book_id] = {"title": title, "author": author, "publication_year": publication_year, "publisher": publisher, "stock": stock, "borrower": None}

def borrow_book():
    borrowed_books = []

    print("Available books:")
    view_all_books()

    borrower_id = input("Enter borrower ID (or type 'back' to return to the main menu): ")
    if borrower_id.lower() == 'back':
        return
    if not borrower_id:
        print("Error: Borrower ID cannot be empty.")
        return

    borrower_name = input("Enter borrower name: ")
    if not borrower_name:
        print("Error: Borrower name cannot be empty.")
        return

    while True:
        book_id = input("Enter book ID to borrow (or type 'back' to return to the main menu): ")
        if book_id.lower() == 'back':
            break
        if not book_id:
            print("Error: Book ID cannot be empty.")
            continue

        if book_id in books:
            if books[book_id]["borrower"] is None and books[book_id]["stock"] > 0:
                books[book_id]["stock"] -= 1
                books[book_id]["borrower"] = borrower_name
                borrowed_books.append({"title": books[book_id]["title"], "book_id": book_id})

                # Ask if the borrower would like to borrow another book
                choice = 0
                while True:
                    another_book = input("Would you like to borrow another book? (yes/no): ").lower()
                    if another_book == 'yes':
                        break
                    elif another_book == 'no':
                        print(f"Thank you {borrower_name}, you have successfully borrowed the following book(s):")
                        for book in borrowed_books:
                            borrow_date = datetime.date.today()
                            return_date = borrow_date + datetime.timedelta(days=14)  # 2 weeks loan period
                            print(f"{book['title']} (ID: {book['book_id']}) - Please return by {return_date}.")
                    while True:
                        print("\nOptions:")
                        print("1. Go back to the main menu")
                        print("2. Close the program")

                        choice = input("\nEnter your choice: ")

                        if choice == "1":
                            break
                        elif choice == "2":
                            print("Goodbye!")
                            exit()
                        else:
                            print("Invalid choice. Please try again.")
                    if choice == "1":
                        break
                if choice == "1":
                    main_menu()

def return_book():
    while True:
        book_id = input("Enter book ID to return (or type 'back' to return to the main menu): ")
        if book_id.lower() == 'back':
            break
        if not book_id:
            print("Error: Book ID cannot be empty.")
            continue

        if book_id in books:
            if books[book_id]["borrower"] is not None:
                books[book_id]["borrower"] = None
                books[book_id]["stock"] += 1
                print(f"Thank you, you have successfully returned the book '{books[book_id]['title']}'.")
                break
            else:
                print("This book is not currently borrowed.")
        else:
            print("Book not found.")

def view_book_details(book_id):
    if book_id in books:
        book = books[book_id]
        table = PrettyTable()
        table.field_names = ["ID", "Title", "Author", "Publication Year", "Publisher", "Stock"]
        table.add_row([book_id, book['title'], book['author'], book['publication_year'], book['publisher'], book['stock']])
        print(table)
    else:
        print("Book not found.")

def view_all_books():
    table = PrettyTable()
    table.field_names = ["ID", "Title", "Author", "Stock"]
    for id, book in books.items():
        table.add_row([id, book['title'], book['author'], book['stock']])
    print(table)

def add_new_book():
    while True:
        book_id = input("Enter book ID (or type 'back' to return to the main menu): ")
        if book_id.lower() == 'back':
            break
        if not book_id:
            print("Error: Book ID cannot be empty.")
            continue
        if book_id in books:
            print("A book with this ID already exists.")
        else:
            title = input("Enter book title: ")
            if not title:
                print("Error: Book title cannot be empty.")
                continue
            author = input("Enter book author: ")
            if not author:
                print("Error: Book author cannot be empty.")
                continue
            publication_year = input("Enter publication year: ")
            if not publication_year:
                print("Error: Publication year cannot be empty.")
                continue
            publisher = input("Enter publisher: ")
            if not publisher:
                print("Error: Publisher cannot be empty.")
                continue
            stock = input("Enter stock: ")
            if not stock:
                print("Error: Stock cannot be empty.")
                continue
            stock = int(stock)
            create_book(book_id, title, author, publication_year, publisher, stock)
            print(f"Book '{title}' by {author} has been successfully added with ID {book_id} and {stock} copies in stock.")
            break

def delete_book():
    while True:
        view_all_books()
        delete_books = input("Enter Book ID you want to delete (or type 'back' to return to the main menu): ")
        if delete_books.lower() == 'back':
            break
        if delete_books in books:
            print(f'You have successfully delete {books[delete_books]["title"]}')
            books.pop(delete_books)
            choice = input("Would you like to delete another book? (yes/no): ").lower()
            if choice == 'yes':
                continue
            elif choice == 'no':
                break
        else:
            print('A book with this ID does not exists.')

def main_menu():
    while True:
        print("\nLibrary Book Borrowing System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View book details")
        print("4. View all books")
        print("5. Add a book")
        print("6. Delete book")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            book_id = input("Enter book ID: ")
            view_book_details(book_id)
        elif choice == "4":
            view_all_books()
        elif choice == "5":
            add_new_book()
        elif choice == "6":
            delete_book()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

books = {}

# Add initial books
create_book("0001", "Love for Imperfect Things", "Haemin Sunim", 2018, "Penguin Life", 5)
create_book("0002", "The School for Broken Hearts", "Haemin Sunim", 2022, "Penguin Books", 3)
create_book("0003", "The Little Book of Hygge", "Meik Wiking", 2016, "Penguin Books", 1)
create_book("0004", "Algoritma dan Pemrograman Menggunakan Python", "Arik Kurniawati", 2016, "Deepublish", 6)
create_book("0005", "Emotional Intelligence", "Daniel Goleman", 1995, "Bantam Books", 6)
create_book("0006", "Ikigai", "Hector Garcia & Francesc Miralles", 2017, "Penguin Books", 5)
create_book("0007", "Sapiens, a Brief History of Humankind", "Yuval Noah Harari", 2011, "Dvir Publishing House Ltd.", 8)
create_book("0008", "Milk and Honey", "Rupi Kaur", 2014, "Andrews McMeel Publishing", 2)
create_book("0009", "Kamu Terlalu Banyak Bercanda", "Marchella FP", 2019, "PT Kebahagiaan Itu Sederhana", 2)
create_book("0010", "The 5AM Club", "Robin Sharma", 2018, "Harper Collins", 2)

# Run the menu-driven interface
main_menu()