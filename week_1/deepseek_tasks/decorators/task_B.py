"""
Напишите декоратор cache_result, который кэширует результат функции при первом вызове и возвращает сохраненное
значение при последующих вызовах (без повторного выполнения функции).
Пример:

@cache_result
def calculate(a, b):
    return a + b  # должно выполняться только один раз для одинаковых a и b
"""


def cache_result(func):
    cache = {}

    def inner(*args):
        if tuple(args) in cache:
            print('returning cached result')
            return cache[tuple(args)]
        else:
            print('calculating')
            result = func(*args)
            cache[tuple(args)] = result
            return result
    return inner


@cache_result
def calculate(a, b):
    return a + b


if __name__ == '__main__':
    print(calculate(1, 2))
    print(calculate(1, 2))
    print(calculate(10, 20))
    print(calculate(10, 20))

