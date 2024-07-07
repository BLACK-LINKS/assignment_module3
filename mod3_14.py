def second_smallest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]

numbers = [12, 13, 1, 10, 34, 16]
print("Original List:", numbers)
print("Second smallest number:", second_smallest(numbers))
