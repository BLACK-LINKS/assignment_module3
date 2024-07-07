l = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
new_value = 0

l = [(t[0], t[1], new_value) for t in l]

print("New List:", l)
