tuple_list = [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]
list1, list2, list3 = zip(*tuple_list)
print(list1, list2, list3)
