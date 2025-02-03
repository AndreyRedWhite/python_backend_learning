"""
Ты пишешь калькулятор для работы с математическими операциями. В нём есть функция умножения:

def multiply(a, b):
    return a * b
Используя functools.partial, создай две новых функции:

double() — умножает число на 2.
triple() — умножает число на 3.

Ожидаемый результат:
print(double(5))  # 10
print(triple(5))  # 15
"""

from functools import partial


def multiply(a, b):
    return a * b


if __name__ == '__main__':
    double = partial(multiply, 2)
    triple = partial(multiply, 3)

    print(double(5))
    print(triple(5))