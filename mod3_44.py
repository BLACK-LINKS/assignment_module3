import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}

for combination in itertools.product(*d.values()):
    print(''.join(combination))
