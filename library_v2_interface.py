import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from library_v2 import Library

class LibraryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.library = Library()
        self.init_ui()

    def init_ui(self):
        # Labels
        self.label_title = QLabel("Title:")
        self.label_author = QLabel("Author:")
        self.label_release_year = QLabel("Release Year:")
        self.label_num_pages = QLabel("Number of Pages:")
        self.label_book_name = QLabel("Book Name:")

        # Line Edits
        self.lineedit_title = QLineEdit()
        self.lineedit_author = QLineEdit()
        self.lineedit_release_year = QLineEdit()
        self.lineedit_num_pages = QLineEdit()
        self.lineedit_book_name = QLineEdit()

        # Buttons
        self.button_list_books = QPushButton("List Books")
        self.button_add_book = QPushButton("Add Book")
        self.button_remove_book = QPushButton("Remove Book")

        # Button Connections
        self.button_list_books.clicked.connect(self.list_books)
        self.button_add_book.clicked.connect(self.add_book)
        self.button_remove_book.clicked.connect(self.remove_book)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button_list_books)
        layout.addWidget(self.button_add_book)
        layout.addWidget(self.button_remove_book)
        
        layout_input = QVBoxLayout()
        layout_input.addWidget(self.label_title)
        layout_input.addWidget(self.lineedit_title)
        layout_input.addWidget(self.label_author)
        layout_input.addWidget(self.lineedit_author)
        layout_input.addWidget(self.label_release_year)
        layout_input.addWidget(self.lineedit_release_year)
        layout_input.addWidget(self.label_num_pages)
        layout_input.addWidget(self.lineedit_num_pages)
        layout_input.addWidget(self.label_book_name)
        layout_input.addWidget(self.lineedit_book_name)

        layout.addLayout(layout_input)
        self.setLayout(layout)

    def list_books(self):
        self.library.list_books()

    def add_book(self):
        title = self.lineedit_title.text()
        author = self.lineedit_author.text()
        release_year = self.lineedit_release_year.text()
        num_pages = self.lineedit_num_pages.text()
        book = [title, author, release_year, num_pages]
        self.library.add_book(book)

    def remove_book(self):
        book_name = self.lineedit_book_name.text()
        self.library.del_book(book_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryGUI()
    window.show()
    sys.exit(app.exec_())
