import random

file_path = input("Enter the path to your file: ")

with open(file_path, 'r') as f:
    lines = f.readlines()
print(random.choice(lines).strip())
