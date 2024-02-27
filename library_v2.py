class Library:
    def __init__(self, file_name="books.txt"):
        """Initialize the Library with a file name and an empty book list."""
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')  # Open the file for reading and appending
        self.book_list = list()  # Initialize an empty list to store books

    def __del__(self):
        """Destructor to close the file when the object is deleted."""
        self.file.close()

    def read_books(self):
        """Read the books from the file and populate the book list."""
        self.file.seek(0)  # Move the file pointer to the beginning
        # Read each line from the file, strip newline characters, and split by comma to get book details
        self.book_list = [list(book.rstrip("\n").split(',')) for book in self.file.readlines() if book.strip()]

    def list_books(self):
        """List all the books stored in the library."""
        try:
            print("Name of Book".center(41, " ") + "|" + "Author of Book".center(39, " "))
            self.read_books()  # Read books from the file
            for i, book in enumerate(self.book_list):
                print(f'{i + 1}.' + book[0].ljust(39) + "|" + book[1].ljust(39))
        except Exception as e:
            print("\nError occurred while listing the Books\n" + str(e))

    def add_book(self, book: list):
        """Add a new book to the library."""
        try:
            # Write the book details to the file separated by commas
            self.file.write("\n" + ",".join(book))
            print("\nThe Book Successfully Added to Library")
        except Exception as e:
            print("\nError occurred while adding the Book\n" + str(e))

    def del_book(self, book_title: str):
        """Remove a book from the library."""
        try:
            self.read_books()  # Read books from the file
            found_books = [book for book in self.book_list if book[0].lower() == book_title.lower()]
            if found_books:
                for book in found_books:
                    self.book_list.remove(book)  # Remove the book from the list
                self.file.seek(0)  # Move the file pointer to the beginning
                self.file.truncate()  # Clear the file contents
                # Write the updated book list to the file
                self.file.writelines([",".join(book) + "\n" for book in self.book_list])
                print(f"\n'{book_title}' Successfully Removed From Library")
            else:
                print(f"\nNo books found with the title '{book_title}'")
        except Exception as e:
            print("\nError occurred while removing the Book\n" + str(e))

    def get_matching_books(self, search_title: str):
        """Find books matching the given search title."""
        try:
            self.read_books()  # Read books from the file
            # Return a list of books where the search title is found (case-insensitive)
            return [book for book in self.book_list if search_title.lower() in book[0].lower()]
        except Exception as e:
            print("\nError occurred while searching for matching books\n" + str(e))
