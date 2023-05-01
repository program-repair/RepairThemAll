def remove_extras(lst):
    rev_lst=lst.copy()
    rev_lst.reverse()
    ori_len=len(lst)
    new_lst=lst.copy()
    for i in range(ori_len):
        if rev_lst[i] in rev_lst[i+1:]:
            new_lst.pop(ori_len-i-1)
    return new_lst
