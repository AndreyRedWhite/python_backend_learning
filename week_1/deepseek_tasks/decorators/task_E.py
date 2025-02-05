"""
Реализуйте декоратор delay(seconds), который добавляет задержку в seconds секунд перед выполнением функции.
Пример:

@delay(2)
def some_func():
    print("Done!")

some_func()  # выполнится через 2 секунды
"""

from time import sleep


def delay(n):

    def decorator(func):
        def inner(*args, **kwargs):
            print(f'sleeping for {n} seconds')
            sleep(n)
            return func(*args, **kwargs)
        return inner
    return decorator


@delay(3)
def some_func():
    print("Done!")


if __name__ == '__main__':
    some_func()