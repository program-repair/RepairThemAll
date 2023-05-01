def remove_extras(lst):
    new_lst = []
    for i in range (len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst
print(remove_extras([1,5,1,1,3,2]))
