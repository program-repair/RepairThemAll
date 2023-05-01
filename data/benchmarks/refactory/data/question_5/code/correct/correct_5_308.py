def sort_descending(lst):
    new_lst = []
    while lst:
        largest = lst[0]
        for i in range(len(lst)):
            if lst[i] > largest:
                largest = lst[i]
        lst.remove(largest)
        new_lst.append(largest)
    return new_lst

def top_k(lst, k):
    lst = sort_descending(lst)
    return lst[:k]
