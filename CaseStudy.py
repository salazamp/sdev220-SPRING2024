from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to store books
books = {}

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book_id = len(books) + 1
    book = {
        'id': book_id,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books[book_id] = book
    return jsonify({'message': 'Book created successfully', 'book': book}), 201

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': list(books.values())}), 200

# Route to get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify({'book': book}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Route to update a book by id
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = books.get(book_id)
    if book:
        book['book_name'] = data.get('book_name', book['book_name'])
        book['author'] = data.get('author', book['author'])
        book['publisher'] = data.get('publisher', book['publisher'])
        return jsonify({'message': 'Book updated successfully', 'book': book}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Route to delete a book by id
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=False)
  