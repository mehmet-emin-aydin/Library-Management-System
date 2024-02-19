class Library:
    def __init__(self, file_name = "books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name,'a+')
        self.book_list = list()
    def __del__(self):
        self.file.close()

    def read_books(self):
        self.file.seek(0)
        self.book_list = [list(book.rstrip("\n").split(',')) for book in self.file.readlines()]

    def list_books(self):
        try:
            print("Name of Book".center(41,)+"|"  + "Author of Book".center(39,))
            self.read_books()
            for i,book in enumerate(Lib.book_list):
                print(f'{i+1}.'+book[0].ljust(39) +"|" +book[1].ljust(39))
        except Exception as e:
            print("\nError accurred while listing the Books\n"+e)
    def add_book(self, book : list ):
        try:
            self.file.write("\n"+",".join(book))
            print("\nThe Book Successfully Added to Library")
        except Exception as e:
            print("\nError accurred while adding the Book\n"+e)
    
    def del_book(self,book_name : str):
        try:
            self.read_books()
            for book in self.book_list:
                if book[0].lower().find(book_name.lower()) !=-1:
                    remove = input(f'{book[0]}\nDo you want to remove this book from the Library:(Y/N)').lower()
                    if remove == 'y':
                        self.book_list.remove(book)
                        self.file.seek(0)
                        self.file.truncate()
                        self.file.writelines([",".join(book)+"\n" if i<len(self.book_list)-1  else ",".join(book) for i,book in enumerate(self.book_list) ])
                        print(f'\n{book[0]} Successfully Removed From Library')
                    found = True
            if not found:
                print("\nThis book does not exist")
        except Exception as e:
            print("\nError accurred while removing the Book\n"+e)
                


Lib = Library()

choice = '1'
while (choice != 'q'):
    choice = input("\n"+"MENU".center(15,"*") +"\n1.List Books\n2.Add Books\n3.Remove Book\nPress Q to exit\nEnter the action you want to perform:\t" ).lower()
    match choice:
        case '1':
            Lib.list_books()
        case '2':
            book = [input("Enter The Name of The Book:"), input("Enter The Author of The Book:"), input("Enter The First Release Year:"), input("Enter The Number of Pages:")]
            Lib.add_book(book)
        case '3':
            Lib.del_book(input("Enter The Name of The Book:"))
        case 'q':
            exit(1)
        case default:
            print("Invalid choice")

    