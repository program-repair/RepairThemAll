def top_k(lst, k):
    newlst = []
    while lst:
        largest = lst[0]
        for number in lst:
            if number > largest:
                largest = number
        lst.remove(largest)
        newlst.append(largest)
    result = []
    for counter in range(k):
        result = result + [newlst[counter],]
    return result
