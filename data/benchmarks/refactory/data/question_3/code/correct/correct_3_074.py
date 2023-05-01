def remove_extras(lst):
    new_list=[]
    for ele in lst:
        if ele not in new_list:
            new_list.append(ele)
    return new_list
