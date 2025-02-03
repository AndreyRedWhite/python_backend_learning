"""
Задание A: Сортировка книг по цене (использование operator.itemgetter)
Описание:
Ты работаешь над системой управления книгами в библиотеке. Данные о книгах хранятся в виде списка словарей, например:

books = [
    {"title": "Book A", "price": 200},
    {"title": "Book B", "price": 100},
    {"title": "Book C", "price": 150},
]
Твоя задача — отсортировать список книг по цене (от самой дешёвой к самой дорогой) с использованием operator.itemgetter.

Ожидаемый результат:
[
    {"title": "Book B", "price": 100},
    {"title": "Book C", "price": 150},
    {"title": "Book A", "price": 200}
]
"""
from pprint import pprint
from operator import itemgetter

books = [
    {"title": "Book A", "price": 200},
    {"title": "Book B", "price": 100},
    {"title": "Book C", "price": 150},
]


books_soted_by_price = sorted(books, key=lambda book: book['price'])
books_sorted_with_itemgetter = sorted(books, key=itemgetter('price'))
pprint(books_soted_by_price)
pprint(books_sorted_with_itemgetter)