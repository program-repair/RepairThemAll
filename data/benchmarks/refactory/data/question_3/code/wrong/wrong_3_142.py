def remove_extras(lst):
    for i in range (0, len(lst)):
        for j in range (i + 1, len(lst)):
            if lst[j] == lst[i]:
                lst.pop(j)
                print (lst)
            else:
                continue
            return remove_extras(lst)
