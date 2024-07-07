def print_unique_values(d):
    unique_values = set(d.values())
    print(unique_values)

d = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 1, 'f': 4}
print_unique_values(d)
