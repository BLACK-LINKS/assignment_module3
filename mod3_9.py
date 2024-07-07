def have_common_member(list1, list2):
    return any(element in list2 for element in list1)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [9, 10, 11, 12]

print("List 1:", list1)
print("List 2:", list2)
print("Do List 1 and List 2 have common members?", have_common_member(list1, list2))

print("List 1:", list1)
print("List 3:", list3)
print("Do List 1 and List 3 have common members?", have_common_member(list1, list3))

print("List 2:", list2)
print("List 3:", list3)
print("Do List 2 and List 3 have common members?", have_common_member(list2, list3))

