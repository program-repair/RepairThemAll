def top_k(lst,k):
    sort = []
    while lst:
        largest = lst[0]
        for element in lst:
            if largest < element:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort[0:k]
