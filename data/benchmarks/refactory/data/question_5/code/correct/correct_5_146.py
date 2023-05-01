def top_k(lst, k):
    # Fill in your code here
    sort_lst = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort_lst.append(biggest)
    return sort_lst[:k]
