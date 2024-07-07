def get_unique_values(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print("Original List:", numbers)
print("Unique Values:", get_unique_values(numbers))
