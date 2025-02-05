"""
Создайте декоратор timer, который измеряет время выполнения функции и выводит его в секундах.
Пример использования:

@timer
def some_function():
    # какой-то код
"""

from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)


def timer(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        logging.info(f'excecution time for {func.__name__} was: {datetime.now() - start}')
        return res
    return inner


@timer
def some_function():
    res = 0
    for i in range(10**8):
        res += i
    return res


if __name__ == '__main__':
    print(some_function())