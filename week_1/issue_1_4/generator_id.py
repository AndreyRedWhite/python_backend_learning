"""
make_id_generator(prefix) возвращает функцию generate_id() , которая при
каждом вызове возвращает "<prefix>_1" , "<prefix>_2" и т.д. (используй
nonlocal ).
"""


def make_id_generator(prefix):
    id = 0

    def generate_id():
        nonlocal id
        id += 1
        return f'{prefix}_{id}'

    return generate_id


if __name__ == '__main__':
    user_gen = make_id_generator('user')

    userlist2 = [user_gen() for user_get in range(5)]
    print(userlist2)
