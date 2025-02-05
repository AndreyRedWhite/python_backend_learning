"""
Создайте декоратор repeat(n), который вызывает декорируемую функцию n раз подряд.
Пример:

@repeat(3)
def say_hello():
    print("Hello!")

# Выведет "Hello!" три раза.
"""


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for r in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(2)
def say_hello():
    print('Hello!')


if __name__ == '__main__':
    say_hello()