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
    book_id = int(input("Enter book id:"))
    name = input("Enter book name:")
    author = input("Enter author name:")
    status = "Available"

    book = {
        "id" : book_id,
        "name" : name,
        "author" : author,
        "status" : status
    }

    books.append(book)


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
    print(" 1. Using book id\n 2. Using book name\n 3. Using author name \n 4. Using book status")
    choice = int(input("How do you want to search a book: "))


    if choice == 1:
        found = False
        book_id = int(input("Enter book id: "))
        print()
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
    else:
            print("Invalid Choice!!")

    

while True:

    print("================================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("================================")
    print()
    
    print(" 1. Add Book\n 2. View Books\n 3. Search Book\n 4. Issue Book\n 5. Return Book\n 6. Remove Book\n 7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    # elif choice == 4:
    #     issue_book()
    # elif choice == 5:
    #     return_book()
    # elif choice == 6:
    #     remove_book()
    elif choice == 7:
        break
    else:
        print("Invalid Choice")
    

