class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')
        self.book_list = list()

    def __del__(self):
        self.file.close()

    def read_books(self):
        self.file.seek(0)
        self.book_list = [list(book.rstrip("\n").split(',')) for book in self.file.readlines()]

    def list_books(self):
        try:
            print("Name of Book".center(41, " ") + "|" + "Author of Book".center(39, " "))
            self.read_books()
            for i, book in enumerate(self.book_list):
                print(f'{i + 1}.' + book[0].ljust(39) + "|" + book[1].ljust(39))
        except Exception as e:
            print("\nError occurred while listing the Books\n" + str(e))

    def add_book(self, book: list):
        try:
            self.file.write("\n" + ",".join(book))
            print("\nThe Book Successfully Added to Library")
        except Exception as e:
            print("\nError occurred while adding the Book\n" + str(e))

    def del_book(self, book_title: str):
        try:
            self.read_books()
            found_books = [book for book in self.book_list if book[0].lower() == book_title.lower()]
            if found_books:
                for book in found_books:
                    self.book_list.remove(book)
                self.file.seek(0)
                self.file.truncate()
                self.file.writelines([",".join(book) + "\n" for book in self.book_list])
                print(f"\n'{book_title}' Successfully Removed From Library")
            else:
                print(f"\nNo books found with the title '{book_title}'")
        except Exception as e:
            print("\nError occurred while removing the Book\n" + str(e))

    def get_matching_books(self, search_title: str):
        try:
            self.read_books()
            return [book for book in self.book_list if search_title.lower() in book[0].lower()]
        except Exception as e:
            print("\nError occurred while searching for matching books\n" + str(e))
