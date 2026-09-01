# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. 
# Show that your program doesnt persist books after the program is stoppeds

class Library:

    def __init__(self):
        self.no_of_books = 0
        self.books = []


    def printBooks(self):
        for book in self.books:
            print(book)

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def getNoOfBooks(self):
        return self.no_of_books

library = Library()
library.addBook("Java")
library.addBook("Python")
library.addBook("Harry Potter vol I")
library.printBooks()
print()
print("Number of books :- ",library.getNoOfBooks())

digital_library = Library()

digital_library.addBook("James Bond Vol I")
digital_library.addBook("Noddy Vol II")
digital_library.addBook("A Hate Story")

print()
digital_library.printBooks()
print()
print(digital_library.getNoOfBooks())