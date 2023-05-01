def remove_extras(lst):
    count=0
    rev_lst=lst.reverse()
    ori_len=len(lst)
    for i in range(ori_len):
        if rev_lst[i] in rev_lst[i+1:]:
            lst.pop(ori_len-i-1)
    return lst
