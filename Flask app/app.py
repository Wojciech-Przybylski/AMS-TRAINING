from flask import Flask, render_template, request

app = Flask(__name__)


class Book:
    books = []

    def __init__(self, title, pages, isbn, genre, author="Unknown"):
        ...
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.genre = genre
        self.author = author
        Book.books.append(self)

    @staticmethod
    def valid_isbn(isbn):
        ...
        digits = ''.join(isbn.split('-'))
        if len(digits) != 13:
            return False
        diglist = [int(digit) for digit in digits]
        return ((sum([diglist[i] for i in range(12) if i % 2 == 0]) + 3 * sum(
            [diglist[i] for i in range(12) if i % 2 != 0]) + diglist[-1]) % 10) == 0

    @staticmethod
    def search(author):
        ...
        return list(filter(lambda book: book.author == author, Book.books))

    def __str__(self):
        ...
        return f"Written by {self.author}, {self.title} is a gripping {self.pages}-page {self.genre} novel"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('add_book_form.html')
    else:
        return render_template('home.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages = int(request.form['pages'])
        genre = request.form['genre']
        isbn = request.form['isbn']

        # Create a new Book object with the form data
        new_book = Book(title, pages, isbn, genre, author)
        # Save the new book to your database or data structure
        # (e.g., append it to a list of all books)

        # Redirect to a success page or render a template with book details
        return f"Book '{new_book.title}' by {new_book.author} added successfully!"

    # If it's a GET request, show the form to add a new book
    return render_template('add_book_form.html')


if __name__ == '__main__':
    app.run(debug=True)
