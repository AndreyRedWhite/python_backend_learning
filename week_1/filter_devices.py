"""
Задание A: Фильтр с гибкими критериями
Есть список словарей devices = [{'hostname': 'R1', 'ip': '10.1.1.1'}, ...] .
Напиши функцию filter_devices(devices, **kwargs) , которая возвращает только те
словари, где все критерии совпадают.
Пример: filter_devices(devices, hostname='R1', ip='10.1.1.1') → фильтрует по
обоим параметрам.
"""

from pprint import pprint


def filter_devices(device_list: list[dict], **kwargs) -> list[dict]:
    """
    Функция принимает на вход список словарей устройств, проверяет каждый словарь на соответствие условий из
    переданных аргументов, если таковые переданы. Возвращает отфильтрованный список словарей
    """

    # Если никаких аргументов для фильрта не задано - возвращаем исходный список
    if not kwargs:
        return device_list

    result = []
    # Итерируемся по словарям, изначально каждый считаем подходящий под критерии
    for dev in device_list:
        match = True
        for k, v in kwargs.items():
            if dev.get(k) != v:
                match = False
                break
        if match:
            result.append(dev)
    return result


if __name__ == '__main__':
    devices = [
        {'hostname': 'R1', 'ip': '10.1.1.1', 'vendor': 'Cisco'},
        {'hostname': 'R2', 'ip': '10.1.2.1', 'vendor': 'Juniper'},
        {'hostname': 'R3', 'ip': '10.1.3.1', 'vendor': 'Huawei'},
        {'hostname': 'SW1', 'ip': '10.1.1.1', 'vendor': 'Fortinet'}
    ]

    pprint(filter_devices(devices)) # возвращает исходный список
    pprint(filter_devices(devices, ip='10.1.1.1')) # вернет 1 и 4 словарь
    pprint(filter_devices(devices, ip='10.1.1.1', vendor='Fortinet')) # вернет только 4-ый словарь
