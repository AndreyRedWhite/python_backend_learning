"""
Task A: LEGB and nested functions
Description
Write a function outer_func with an inner function inner_func. Experiment with global and nonlocal to see how they
affect variable scope.

def outer_func():
    x = 10
    def inner_func():
        nonlocal x
        x = 20
        print("inner x =", x)
    inner_func()
    print("outer x =", x)
"""

test_str = 'global var'


def outher_func(x: int):
    print(f'calling an outer func with param: {x=}')

    def inner_func(y: int):
        nonlocal x
        print(f'we got this param from outer: {x}')
        x += 100
        print(f'and we easily changed it to new value: {x=}.\nAlso get this: {y=}')
        return x * y
    return inner_func


if __name__ == '__main__':
    data1 = outher_func(5)
    data2 = data1(3)
    print(data2)

