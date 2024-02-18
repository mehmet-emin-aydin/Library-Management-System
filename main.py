class Library:
    def __init__(self) -> None:
        self.file =  open("books.txt", "a+")
    def __del__(self):
        self.file.close()

    def read_file(self):
        self.file.seek(0)
        self.book_list = self.file.readlines()
        for i in range(len(self.book_list)):
            self.book_list[i] = self.book_list[i].rstrip('\n')
            self.book_list[i] = list(self.book_list[i].split(","))
            
    def add_book(self, book_info : list) -> bool:
        try:
            self.read_file()
            self.book_list.append(book_info)
            self.file.write("\n"+", ".join(self.book_list[-1]))
            return True
        except Exception as e:
            print(f"Error occurred while adding a new book:\n{e}")
            return False
        
    def remove_book(self, book_name : str) -> bool:
        try:
            self.read_file()
            found = False
            for  i in range(len(self.book_list)-1,-1,-1):
                if book_name.lower().find(self.book_list[i][0].lower())!=-1:
                    self.book_list.remove(self.book_list[i])
                    found = True
            if not found:
                raise ValueError('Book not Found')
            self.file.seek(0)
            self.file.truncate()
            [self.file.write(", ".join(book) + "\n") if i < len(self.book_list) - 1 else self.file.write(", ".join(book)) for i, book in enumerate(self.book_list)]
            return True
        except Exception as e:
            print(f"Error occurred while removing the book:\n{e}")
            return False
        '''
        try:
            self.read_file()
            index = -1
            for i in range(len(self.book_list)):
                if int(self.book_list[i][0]) == book_id:
                    index = i
            if index == -1:
                raise ValueError(f"No book with ID {book_id} found.")
            del self.book_list[index]
            # Rearrange the IDs of remaining books
            for i in range(index, len(self.book_list)):
                self.book_list[i][0] = str((int(self.book_list[i][0])-1))
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines("\n".join([",".join(x) for x in self.book_list]))
            return True
        except Exception as e:
            print(f"Error occurred while removing a book:\n{e}")
            return False
        '''

lib = Library()
lib.read_file()
print(lib.book_list) # should return the number of books in the


def displayMenu():
    choice = input("Menu".center(40, "*")+"\n1.List books!\n2. Add a book to the library!\n3. Remove a book from the library!\n")
    return choice
choice = ''
while (choice != 'q'):
    choice = displayMenu()
    match choice:
        case  '1':
            lib.read_file()
            print("\nBooks in the library:\n")
            for  line in lib.book_list:
                print("Title: ",line[0], " Author: ",line[1],"\tYear Published: ",line[2],"\n\tNumber of Pages: ",line[3])
                input('\nPress Enter to continue...')
        case '2':
            new_book = [input('Enter Book Title: '), input('Enter Book Author: '), input('Enter the Year Published: '), input('Enter the Number of Pages: ')]
            lib.add_book(new_book)
        case  '3':
            lib.read_file()
            removed_book =  input("Enter Title: ")
            lib.remove_book(removed_book)
        case 'q':
            exit()

del lib