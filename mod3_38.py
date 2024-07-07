def check_multiple_keys(dict, keys):
    if all(key in dict for key in keys):
        print("All keys exist in the dictionary.")
        return True
    else:
        print("Not all keys exist in the dictionary.")
        return False

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys = ['a', 'b', 'c', 'd', 'e']
check_multiple_keys(dict, keys)

keys = ['a', 'b', 'c', 'd', 'f']
check_multiple_keys(dict, keys)
