def remove_extras(lst):
    if lst==[]:
        return []
    new_lst=[lst[0]]
    for i in range(len(lst)):
        a=lst[i]
        for h in range(i,len(lst)):
            if a!=lst[h]:
                ele=lst[h]
                if ele in new_lst:
                    continue
                new_lst.append(ele)
    return new_lst
