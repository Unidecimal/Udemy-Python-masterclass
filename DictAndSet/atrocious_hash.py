data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
    ]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))
# print(ord("A"))


def simple_hash(s: str) -> int:
    """A rediculus simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    """Return the value for a key, or None if the key doen't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get("lemon")
print(value)
value1 = get("grape")
print(value1)
value2 = get("tomato")
print(value2)
value3 = get("banana")
print(value3)