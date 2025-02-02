"""
Задача 1.2: Генератор ID (средняя)
Создайте функцию generate_id, которая:
Принимает prefix (строка), length (длина цифровой части).

Возвращает строку вида "{prefix}-{рандомные_цифры}".

Используйте *args и **kwargs, чтобы можно было передавать параметры в random.choices.

python
Copy
print(generate_id("user", 5)) # user-38471
"""
from string import digits
from random import choices


def generate_id(prefix: str, lenght: int, *args, **kwargs) -> str:
    data = choices(digits, k=lenght, *args, **kwargs)
    return f"{prefix}-{''.join(data)}"


if __name__ == '__main__':
    print(generate_id('user', 5))
    weights = [2 if int(d) % 2 == 0 else 1 for d in digits]
    print(generate_id("order", 3, weights=weights))  # order-624