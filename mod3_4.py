def get_stats(numbers):
    if not numbers:
        return None, None, 0
    return max(numbers), min(numbers), sum(numbers)

numbers = [3, 1, 4, 2, 5]
largest, smallest, total = get_stats(numbers)
print(f"Largest: {largest}, Smallest: {smallest}, Sum: {total}")
