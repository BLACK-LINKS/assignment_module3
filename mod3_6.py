def count_strings(lst):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

strings = ["abcba", "hello", "world", "radar", "xyz", "abba", "cdc"]
print("Count:", count_strings(strings))
