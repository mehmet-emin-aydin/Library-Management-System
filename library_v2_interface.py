import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QStackedLayout, QMessageBox, QHBoxLayout, QFormLayout

from library_v2 import Library

class LibraryGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.library = Library()
        self.init_ui()

    def init_ui(self):
        self.stacked_layout = QStackedLayout()
        self.create_main_menu()
        self.create_list_books_layout()
        self.create_add_book_layout()
        self.create_remove_book_layout()
        self.setLayout(self.stacked_layout)

    def create_main_menu(self):
        buttons = [
            ("List Books", self.list_books),
            ("Add Book", self.show_add_book_form),
            ("Remove Book", self.show_remove_book_layout),
            ("Exit", self.close)
        ]
        self.stacked_layout.addWidget(self.create_widget_with_buttons(buttons))

    def create_list_books_layout(self):
        self.list_books_widget = self.create_widget_with_layout(QVBoxLayout(), [QLabel("Books:")])
        self.stacked_layout.addWidget(self.list_books_widget)

    def create_add_book_layout(self):
        labels = ["Title:", "Author:", "Release Year:", "Number of Pages:"]
        line_edits = [QLineEdit() for _ in range(len(labels))]
        self.line_edits = line_edits
        form_layout = QFormLayout()
        for label, line_edit in zip(labels, line_edits):
            form_layout.addRow(label, line_edit)
        buttons = [("Save", self.save_book), ("Cancel", self.restore_main_menu)]
        button_layout = QHBoxLayout()
        for text, callback in buttons:
            button = QPushButton(text)
            button.clicked.connect(callback)
            button_layout.addWidget(button)
        add_book_layout = QVBoxLayout()
        add_book_layout.addLayout(form_layout)
        add_book_layout.addLayout(button_layout)
        add_book_widget = QWidget()
        add_book_widget.setLayout(add_book_layout)
        self.stacked_layout.addWidget(add_book_widget)

    def create_remove_book_layout(self):
        remove_layout = QVBoxLayout()
        self.lineedit_remove_title = QLineEdit()
        buttons = [("Remove", self.remove_book), ("Cancel", self.restore_main_menu)]
        remove_layout.addWidget(QLabel("Enter the Title of the Book to Remove:"))
        remove_layout.addWidget(self.lineedit_remove_title)
        remove_layout.addStretch(1)
        button_layout = QHBoxLayout()
        for text, callback in buttons:
            button = QPushButton(text)
            button.clicked.connect(callback)
            button_layout.addWidget(button)
        remove_layout.addLayout(button_layout)
        self.remove_book_widget = QWidget()
        self.remove_book_widget.setLayout(remove_layout)
        self.stacked_layout.addWidget(self.remove_book_widget)

    def create_widget_with_buttons(self, button_info):
        layout = QVBoxLayout()
        for text, callback in button_info:
            button = QPushButton(text)
            button.clicked.connect(callback)
            layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def create_widget_with_layout(self, layout, widgets=None):
        if widgets:
            for widget in widgets:
                layout.addWidget(widget)
        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def save_book(self):
        title = self.line_edits[0].text()
        if not title.strip():
            QMessageBox.warning(self, 'Warning', "Please enter the title of the book!")
            return
        book_info = [lineedit.text() for lineedit in self.line_edits]
        self.library.add_book(book_info)
        self.restore_main_menu()

    def list_books(self):
        self.clear_layout(self.list_books_widget.layout())
        self.library.read_books()
        for book in self.library.book_list:
            self.list_books_widget.layout().addWidget(QLabel(f"{book[0]} by {book[1]}"))
        button_close = QPushButton("Close")
        button_close.clicked.connect(self.restore_main_menu)
        self.list_books_widget.layout().addWidget(button_close)
        self.stacked_layout.setCurrentIndex(1)

    def remove_book(self):
        title_to_remove = self.lineedit_remove_title.text()
        if not title_to_remove.strip():
            QMessageBox.warning(self, 'Warning', "Please enter the title of the book to remove!")
            return
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
        self.stacked_layout.setCurrentIndex(0)

    def show_add_book_form(self):
        self.stacked_layout.setCurrentIndex(2)

    def show_remove_book_layout(self):
        self.stacked_layout.setCurrentIndex(3)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryGUI()
    window.show()
    sys.exit(app.exec_())
