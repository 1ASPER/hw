from random import randint

# task 4

data = [randint(-999, 999) for i in range(randint(5, 10))]
print(f"Before: {data}")

def sort_by_last_number(elem: int | float) -> int | None:
    match elem:
        case int() | float() if elem >= 0:
            return abs(elem % 10)
        case _:  # wildcard (default)
            raise ValueError("Error: array consists bad element!")

print(f"After {sorted(data, key=sort_by_last_number)}")

