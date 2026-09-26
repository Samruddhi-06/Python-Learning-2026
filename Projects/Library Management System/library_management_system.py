# Project: Library Management System
# Goal
# Build a console-based program that allows a user to manage books in a library.
# The program should allow you to:
# Add a book
# View all books
# Search for a book
# Issue a book
# Return a book
# Remove a book
# Exit


books = [
    {
        "id" : 1102,
        "name" : "The Guide",
        "author" : "R.K. Narayan",
        "status" : "Available"
    },
    {
        "id" : 121,
        "name" : "A Suitable Boy",
        "author" : "Vikram Seth",
        "status" : "Available"
    },
    {
        "id" : 556,
        "name" : "Wings of Fire",
        "author" : "APJ Abdul Kalam",
        "status" : "Unavailable"
    },
    {
        "id" : 420,
        "name" : "1984",
        "author" : "George Orwell",
        "status" : "Available"
    },
    {
        "id" : 1001,
        "name" : "God of Small Things",
        "author" : "Arundhati Roy",
        "status" : "Unavailable"
    }
]


def add_book():
    while True:
        try:
            book_id = int(input("Enter book id:"))
        except ValueError:
            print("Invalid book id!!")
            print()
            continue
        break

    for book in books:
        if book["id"] == book_id:
            print(f"Book with id {book_id} is already present.")
            print()
            return 

    
    name = input("Enter book name: ").strip()

    if not name:
        print("Book name cannot be empty!")
        return
    
    author = input("Enter author name:").strip()

    if not author:
        print("Author name cannot be empty!")
        return

    status = "Available"

    book = {
        "id" : book_id,
        "name" : name,
        "author" : author,
        "status" : status
    }

    books.append(book)
    print("New Book Added.")
    print()


def view_books():
    print("================================")
    print("ALL BOOKS")
    print("================================")
    print()

    for book in books:
        print(book["id"])
        print(book["name"])
        print(book["author"])
        print(book["status"])
        print("------------------------------")

def search_book():

    while True:
        print(" 1. Using book id\n 2. Using book name\n 3. Using author name \n 4. Using book status")
        try:
            choice = int(input("How do you want to search a book: "))
            print()
        except ValueError:
            print("Enter a valid choice(1-4)!!")
            print()
            continue

        if choice < 1 or choice > 4:
            print("Enter a valid choice(1-4)!!")
            print()
            continue
        break

    if choice == 1:
        found = False
        while True:
            try:
                book_id = int(input("Enter book id: "))
                print()
            except ValueError:
                print("Invalid id!!")
                print()
                continue
            break

        for book in books:
            if book["id"] == book_id:
                print(book["id"])
                print(book["name"])
                print(book["author"])
                print(book["status"])
                print("------------------------------")
                found = True
        if not found:
            print("Book not found!!")
    elif choice == 2:
        found = False
        name = input("Enter book name: ")
        print()
        for book in books:
            if book["name"] == name:
                print(book["id"])
                print(book["name"])
                print(book["author"])
                print(book["status"])
                print("------------------------------")
                found = True
        if not found:
            print("Book not found!!")
    elif choice == 3:
        found = False
        author = input("Enter author name: ")
        print()
        for book in books:
            if book["author"] == author:
                print(book["id"])
                print(book["name"])
                print(book["author"])
                print(book["status"])
                print("------------------------------")
                found = True
        if not found:
            print("Book not found!!")
    elif choice == 4:
        found = False
        status = input("Enter book status: ")
        print()
        for book in books:
            if book["status"] == status:
                print(book["id"])
                print(book["name"])
                print(book["author"])
                print(book["status"])
                print("------------------------------")
                found = True
        if not found:
            print("Book not found!!")



def issue_book():
    while True:
        try:
            book_id = int(input("Enter the book id: "))
            print()
        except ValueError:
            print("Invalid book id!!")
            print()
            continue
        break
    
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True  
            if book["status"] == "Available":
                book["status"] = "Unavailable"
                print("Book issued.")
                print()
            elif book["status"] == "Unavailable":
                print("Sorry! The book is unavailable.")
                print()
    if not found:
        print("Book not found.")
        print()


def return_book():
    while True:
        try:
            book_id = int(input("Enter the book_id: "))
            print()
        except ValueError:
            print("Invalid book id!!")
            print()
            continue
        break
    
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True
            if book["status"] == "Unavailable":
                print("Book returned successfully!")
                print()
                book["status"] = "Available"
            elif book["status"] == "Available":
                print("This book was never issued.")
                print()
    if not found:
        print("Book not found.")
        print()

def remove_book():
    while True:
        try:
            book_id = int(input("Enter the book id: "))
            print()
        except ValueError:
            print("Invalid book id!!")
            print()
            continue
        break
    
    found = False

    for book in books:
        if book["id"] == book_id:
            found = True
            books.remove(book)
            print(f"Book with id {book_id} has been removed.")
            print()
            break
    if not found:    
        print("Book not found.")
        



while True:

    print("================================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("================================")
    print()
    
    print(" 1. Add Book\n 2. View Books\n 3. Search Book\n 4. Issue Book\n 5. Return Book\n 6. Remove Book\n 7. Exit")
    try:
        choice = int(input("Enter your choice: "))
        print()
    except ValueError:
        print("Enter a valid choice (1-7)!!")
        print()
        continue

    if choice < 1 or choice > 7:
        print("Enter a valid choice (1-7)!!")
        print()
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        remove_book()
    elif choice == 7:
        break   

