def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print("Original list:", numbers)
print("List after removing duplicates:", remove_duplicates(numbers))
