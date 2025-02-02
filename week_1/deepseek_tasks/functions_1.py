"""
Задача 1.1: Форматирование текста (легкая)
Напишите функцию format_phone, которая принимает строку с номером телефона (10 цифр) и возвращает его в формате: "+7 (XXX) XXX-XX-XX".
python
Copy
print(format_phone("9123456789")) # +7 (912) 345-67-89
"""


def format_phone(phone: str) -> str:
    return f"+7 ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9::]} "


if __name__ == '__main__':
    print(format_phone('89152415169'))