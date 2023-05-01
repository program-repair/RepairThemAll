def top_k(lst, k):
    
    sort = []
    
    while lst:

        largest = lst[0]

        for x in lst:

            if x > largest:

                largest = x

        lst.remove(largest)

        sort.append(largest)

    return sort[:k]
