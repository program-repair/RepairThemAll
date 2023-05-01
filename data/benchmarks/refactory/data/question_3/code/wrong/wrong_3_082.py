def remove_extras(lst):
    new_lst = [lst[0]]
    for i in range(0,len(lst)):
        a=lst[i]
        for h in range(i,len(lst)):
            if a!=lst[h]:
                ele=lst[h]
                new_lst.append(ele)       
        return new_lst
    return new_lst
