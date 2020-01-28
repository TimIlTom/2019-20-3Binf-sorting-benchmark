from Book import Book
from bubble_sort import bubble_sort
from selection_sort_book import selection_sort

book1 = Book("Canzoniere", "Petrarca")
book2 = Book("Divina Commedia", "Dante")
book3 = Book("Decameron", "Boccaccio")

book_list = [book1, book2, book3]

selection_sort(book_list)