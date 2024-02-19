import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QStackedLayout, QMessageBox

from library_v2 import Library

class LibraryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.library = Library()
        self.init_ui()

    def init_ui(self):
        self.stacked_layout = QStackedLayout()

        # Main Menu UI
        self.main_menu_widget = QWidget()
        main_layout = QVBoxLayout()
        self.button_list_books = QPushButton("List Books")
        self.button_add_book = QPushButton("Add Book")
        self.button_remove_book = QPushButton("Remove Book")
        self.button_exit = QPushButton("Exit")
        self.button_list_books.clicked.connect(self.list_books)
        self.button_add_book.clicked.connect(self.show_add_book_form)
        self.button_remove_book.clicked.connect(self.show_remove_book_layout)
        self.button_exit.clicked.connect(self.close)
        main_layout.addWidget(self.button_list_books)
        main_layout.addWidget(self.button_add_book)
        main_layout.addWidget(self.button_remove_book)
        main_layout.addWidget(self.button_exit)
        self.main_menu_widget.setLayout(main_layout)

        # List Books UI
        self.list_books_widget = QWidget()
        self.list_books_layout = QVBoxLayout()
        self.label_books = QLabel("Books:")
        self.list_books_layout.addWidget(self.label_books)
        self.list_books_widget.setLayout(self.list_books_layout)

        # Add Book UI
        self.add_book_widget = QWidget()
        add_book_layout = QVBoxLayout()
        self.label_title = QLabel("Title:")
        self.label_author = QLabel("Author:")
        self.label_release_year = QLabel("Release Year:")
        self.label_num_pages = QLabel("Number of Pages:")
        self.lineedit_title = QLineEdit()
        self.lineedit_author = QLineEdit()
        self.lineedit_release_year = QLineEdit()
        self.lineedit_num_pages = QLineEdit()
        self.button_save = QPushButton("Save")
        self.button_cancel = QPushButton("Cancel")
        self.button_save.clicked.connect(self.save_book)
        self.button_cancel.clicked.connect(self.restore_main_menu)
        add_book_layout.addWidget(self.label_title)
        add_book_layout.addWidget(self.lineedit_title)
        add_book_layout.addWidget(self.label_author)
        add_book_layout.addWidget(self.lineedit_author)
        add_book_layout.addWidget(self.label_release_year)
        add_book_layout.addWidget(self.lineedit_release_year)
        add_book_layout.addWidget(self.label_num_pages)
        add_book_layout.addWidget(self.lineedit_num_pages)
        add_book_layout.addWidget(self.button_save)
        add_book_layout.addWidget(self.button_cancel)
        self.add_book_widget.setLayout(add_book_layout)

        # Remove Book UI
        self.remove_book_widget = QWidget()
        remove_book_layout = QVBoxLayout()
        self.label_remove_title = QLabel("Enter the Title of the Book to Remove:")
        self.lineedit_remove_title = QLineEdit()
        self.button_remove = QPushButton("Remove")
        self.button_cancel1 = QPushButton("Cancel")
        self.button_remove.clicked.connect(self.remove_book)
        self.button_cancel1.clicked.connect(self.restore_main_menu)
        remove_book_layout.addWidget(self.label_remove_title)
        remove_book_layout.addWidget(self.lineedit_remove_title)
        remove_book_layout.addWidget(self.button_remove)
        remove_book_layout.addWidget(self.button_cancel1)
        self.remove_book_widget.setLayout(remove_book_layout)

        self.stacked_layout.addWidget(self.main_menu_widget)
        self.stacked_layout.addWidget(self.list_books_widget)
        self.stacked_layout.addWidget(self.add_book_widget)
        self.stacked_layout.addWidget(self.remove_book_widget)

        self.setLayout(self.stacked_layout)

    def show_add_book_form(self):
        self.stacked_layout.setCurrentIndex(2)  # Show add book form

    def save_book(self):
        title = self.lineedit_title.text()
        author = self.lineedit_author.text()
        release_year = self.lineedit_release_year.text()
        num_pages = self.lineedit_num_pages.text()
        book_info = [title, author, release_year, num_pages]
        self.library.add_book(book_info)
        self.restore_main_menu()

    def list_books(self):
        # Clear the previous list of books
        for i in reversed(range(self.list_books_layout.count())):
            widget = self.list_books_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        self.library.read_books()
        for book in self.library.book_list:
            self.list_books_layout.addWidget(QLabel(f"{book[0]} by {book[1]}"))
        self.button_close = QPushButton("Close")
        self.button_close.clicked.connect(self.restore_main_menu)
        self.list_books_layout.addWidget(self.button_close)
        self.stacked_layout.setCurrentIndex(1)  # Show list of books

    def show_remove_book_form(self):
        self.stacked_layout.setCurrentIndex(3)  # Show remove book form

    def remove_book(self):
        title_to_remove = self.lineedit_remove_title.text()
        matching_books = self.library.get_matching_books(title_to_remove)
        if matching_books:
            for book in matching_books:
                reply = QMessageBox.question(self, 'Confirmation', f"Do you want to remove '{book[0]}' by {book[1]}?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.library.del_book(book[0])
                    QMessageBox.information(self, 'Information', f"'{book[0]}' removed successfully!")
        else:
            QMessageBox.warning(self, 'Warning', f"No books found with the title '{title_to_remove}'!")

    def restore_main_menu(self):
        self.stacked_layout.setCurrentIndex(0)  # Show main menu

    def show_remove_book_layout(self):
        self.stacked_layout.setCurrentIndex(3)  # Show remove book form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryGUI()
    window.show()
    sys.exit(app.exec_())
