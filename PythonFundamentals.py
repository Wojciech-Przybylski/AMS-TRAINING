book_dictionary = { 'Harper Lee':['To Kill a Mockingbird'], 'J. R. R. Tolkien':['The Lord of the Rings'], 'George Orwell':['1984'], 'Emily Brontë':['Wuthering Heights'], 'Frank Herbert':['Dune'], 'Miguel de Cervantes':['Don Quixote'], 'Scott Fitzgerald':['The Great Gatsby'], 'Charlotte Brontë':['Jane Eyre']}

author_choice = input(f"Choose from the list of authors available: ")
print(','.join(book_dictionary[author_choice]))