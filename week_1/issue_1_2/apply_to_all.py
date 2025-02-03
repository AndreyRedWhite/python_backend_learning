"""
Implement apply_to_all(func, items) that returns a list of func(item) for each item in items.

def uppercase(s): return s.upper()

print(apply_to_all(uppercase, ["hello", "world"]))
# => ["HELLO", "WORLD"]
"""


def apply_to_all(func: callable, items: iter) -> callable:
    """
    function, that works the same as map()
    """
    result = []
    for item in items:
        result.append(func(item))
    return result


print(apply_to_all(str.upper, ['hello', 'word']))
print(apply_to_all(lambda x: x * 2, [1, 2, 3]))
print(list(map(lambda x: x * x, [1, 2, 3])))
