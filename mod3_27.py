def find_repeated_items(t):
    return [item for item in set(t) if t.count(item) > 1]

t = (1, 2, 3, 2, 4, 5, 5, 6)
print("Repeated items in the tuple:", find_repeated_items(t))
