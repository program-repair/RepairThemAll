def top_k(lst, k):
    # Fill in your code here
    sort = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort[:k]
