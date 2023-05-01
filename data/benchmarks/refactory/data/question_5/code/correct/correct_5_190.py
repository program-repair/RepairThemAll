def sort_no(lst):
    lst_len = len(lst) - 1
    while lst_len > 0:
        for i in range(lst_len):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        lst_len -= 1
    return lst[::-1]
def top_k(lst, k):
    return sort_no(lst)[:k]
