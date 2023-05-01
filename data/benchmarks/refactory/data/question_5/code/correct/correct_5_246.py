def top_k(lst, k):
    sortedlst = []
    while len(sortedlst) != k:
        largest = lst[0]
        for el in lst:
            if el > largest:
                largest = el
        sortedlst.append(largest)
        lst.remove(largest)
    return sortedlst
