"""
Описание:
У тебя есть список чисел:

numbers = [10, -5, 30, -1, 0, 42, -17]
Отфильтровать только положительные числа.
Удвоить каждое из оставшихся значений.
Ожидаемый результат:

[20, 60, 0, 84]
"""


numbers = [10, -5, 30, -1, 0, 42, -17]

positive = list(filter(lambda x: x>=0, numbers))
print(positive)
doubled = list(map(lambda x: x * 2, positive))
print(doubled)