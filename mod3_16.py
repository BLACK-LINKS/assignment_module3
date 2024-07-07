def contains_sublist(lst, sublst):
    return tuple(sublst) in [tuple(lst[i:i+len(sublst)]) for i in range(len(lst))]

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [3, 4, 5]
print("Main List:", main_list)
print("Sub List:", sub_list)
print("Is Sub List present in Main List?", contains_sublist(main_list, sub_list))
