"""
Задание B: Сумматор с разными способами вызова
Функция multi_sum(*numbers, power=1) :
Если power=2 , сначала возводит аргументы в квадрат, затем суммирует.
Пример: multi_sum(1,2,3, power=2) → 14.
"""


def multi_sum(*args, power: int = 1) -> int:
    res = sum([i ** power for i in args])
    return res


if __name__ == '__main__':
    print(multi_sum(1, 2, 3, power=2))
    print(multi_sum(power=2))
    print(multi_sum(11, 23, 34, power=3))