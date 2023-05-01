def remove_extras(lst):
    new_lst=[lst[0]]
    if lst==[]:
        return []
    for i in range(len(lst)):
        a=lst[i]
        for h in range(i,len(lst)):
            if a!=lst[h]:
                ele=lst[h]
                if ele in new_lst:
                    continue
                new_lst.append(ele)
    return new_list
