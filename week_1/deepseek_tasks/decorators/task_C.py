"""
Реализуйте декоратор count_calls, который подсчитывает количество вызовов декорируемой функции и сохраняет это
значение в атрибуте call_count.
Пример:

@count_calls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
print(greet.call_count)  # должно вывести 2
"""


def count_calls(func):

    def inner(*args, **kwargs):
        inner.call_count += 1
        return func(*args, **kwargs)
    inner.call_count = 0
    return inner


@count_calls
def greet(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    greet("Alice")
    greet("Bob")
    print(greet.call_count)  # должно вывести 2
