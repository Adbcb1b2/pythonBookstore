# A Python program that simulates a basic library system where students can borrow and return books.

class Book:
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    # Method to borrow a book
    def borrow(self):
        # If the book is available
        if self.is_available: 
            print(f"The book '{self.title}' by {self.author} has been borrowed.")
            self.is_available = False # Update the availability status
        # If the book is not available
        else: 
            print(f"The book '{self.title}' by {self.author} has already been borrowed.")
    
    # Method to return a book
    def return_book(self):
        # If the book is not available
        if not self.is_available:
            print(f"The book '{self.title}' by {self.author} has been returned.")
            self.is_available = True # Update the availability status
        # If the book is available
        else:
            print(f"The book '{self.title}' by {self.author} has already been returned.")
class Library:
    # Constructor
    def __init__(self):
        self.books = [] # List containting books instances
    
    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"The book '{book.title}' by {book.author} has been added to the library.")

    # Method to List books with their availability status
    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "available" if book.is_available else "not available"
            print(f"'{book.title}' by {book.author} - {status}")

    # Method to search books by title and return if found
    def find_book(self, title):
        # Loop through the books list and check if the title matches (lowercase to ignore case)
        for book in self.books:
            if book.title.lower() == title.lower():
                return book # Return the book instance if found
        return None

    # Method to borrow a book by title
    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            return book.borrow() # Call the borrow method of the book instance which will update the availability status
        else:
            print(f"The book '{title}' is not available in the library.")

    # Method to return a book by title
    def return_book(self, title):
        book = self.find_book(title) # Find the book by title
        # If a book is found, call the return_book method of the book instance which will update the availability status
        if book:
            return book.return_book()
        else: 
            print(f"The book '{title}' is not available in the library.")

def main():
    # Create an instance of library
    library = Library()

    # Create 5 books
    book1 = Book("Amazing book 1", "Author 1")
    book2 = Book("Interesting book 2", "Author 2")
    book3 = Book("Fascinating book 3", "Author 3")
    book4 = Book("Exciting book 4", "Author 4")
    book5 = Book("Incredible book 5", "Author 5")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    # Menu System
    while True:
        print("\n")
        print("Menu System:")
        print("1: View all books")
        print("2: Borrow a book")
        print("3: Return a book")
        print("4: Exit the program")
        

        choice = input("\nEnter your choice: ") # Get user input

        if choice == "1":
            library.list_books()

        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)

        elif choice == "4":
            print("Exiting the program.")
            break # Exit the program

        else:
            ("Invalid menu choice. Please try again.")

if __name__ == "__main__":
    main()