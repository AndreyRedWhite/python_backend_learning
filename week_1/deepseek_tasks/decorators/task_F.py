"""
Напишите декоратор validate_args(type1, type2, ...), который проверяет типы аргументов функции. Если типы не совпадают,
 вызывает TypeError.
Пример:

@validate_args(int, str)
def process_data(num, text):
    pass

process_data(5, "test")  # ок
process_data("5", "test")  # TypeError
"""


def validate_args(*args):

    def decorator(func):
        def inner(*func_args):
            arguments_and_types = list(zip(args, func_args))
            for dec_arg, func_arg in arguments_and_types:
                if not isinstance(func_arg, dec_arg):
                    raise TypeError('аргументы некорректны')
            return func(*func_args)
        return inner
    return decorator


@validate_args(int, str)
def process_data(digit: int, text: str) -> None:
    print(digit, text)


if __name__ == '__main__':
    process_data(5, "test")  # ок
    process_data("5", "test")  # TypeError
