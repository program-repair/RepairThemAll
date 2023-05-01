def top_k(lst, k):
    result = 0
    new_list = []
    while result < k:
        temp = max(lst)
        new_list.append(temp)
        lst.remove(temp)
        result = result + 1
    return new_list
