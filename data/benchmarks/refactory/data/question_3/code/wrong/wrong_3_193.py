def remove_extras(lst):
    count=0
    rev_lst=lst.reverse()
    ori_len=len(lst)
    new_lst=lst.copy()
    for i in range(ori_len):
        if rev_lst[i] in rev_lst[i+1:]:
            new_lst.pop(ori_len-i-1)
    return new_lst
