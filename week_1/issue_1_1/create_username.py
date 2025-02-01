"""
Задание C: Keyword-only и Positional-only
Функция create_user(name, /, *, role="guest") :
name – позиционный, role – keyword-only.
Проверь, что вызов create_user("Alice", role="admin") валиден, а
create_user(name="Alice") – нет.
"""


def create_username(name: str, /, *, role: str = 'guest') -> str:
    return f'User {name} with role {role} was successfully created'


if __name__ == '__main__':
    try:
        print(create_username('Alice', role='admin'))
        print(create_username('John', 'admin'))
    except TypeError as e:
        print(f'error: {e}.\nYou should type role as key argument only')





