"""
B: Кэширование через closure
Декоратор cache_func(func) или функция, которая кэширует результаты вызовов исходной func (проверка (args, kwargs)).
"""


def cache(func):
    calc_results = {}

    def wrapper(*args, **kwargs):
        if args in calc_results:
            return calc_results[args]
        result = func(*args, **kwargs)
        calc_results[args] = result
        return result

    return wrapper


@cache
def slow_calculation(x, y, z):
    print("Calculating...")
    return x ** y ** z


if __name__ == '__main__':
    (slow_calculation(10, 10, 6))  # Calculating 10... → 100
    (slow_calculation(10, 10, 6))  # 100 (взято из кеша, без "Calculating 10...")
