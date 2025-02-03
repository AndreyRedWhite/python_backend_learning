"""
Write dynamic_set(obj, attr, value) and dynamic_get(obj, attr).

If attr not found, dynamic_get returns "Attribute not found".
Example

class Person: pass

p = Person()
dynamic_set(p, "name", "Alice")
print(dynamic_get(p, "name"))  # "Alice"
"""

from typing import Any


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person name={self.name}'


def set_attr(obj, attr: Any, attr_value: Any):
    setattr(obj, attr, attr_value)


def get_attr(obj, attr: Any):
    getattr(obj, attr)


if __name__ == '__main__':
    p = Person('Alice')
    set_attr(p, 'age', 34)
    print(p)
    print(p.age)
    p.gender = 'female'
    print(p.__dict__)

