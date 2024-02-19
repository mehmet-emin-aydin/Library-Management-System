    def list_books(self):
        self.library.read_books()
        list_books_layout = QVBoxLayout()
        list_books_layout.addWidget(self.label_books)
        for book in self.library.book_list:
            list_books_layout.addWidget(QLabel(f"{book[0]} by {book[1]}"))
        list_books_layout.addWidget(self.button_close)
        self.list_books_widget.setLayout(list_books_layout)
        self.stacked_layout.setCurrentIndex(1)  # Show list of books
