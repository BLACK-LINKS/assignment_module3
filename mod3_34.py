def check_key_existence(dict, key):
    if key in dict:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
check_key_existence(dict, key)

key = 'd'
check_key_existence(dict, key)
