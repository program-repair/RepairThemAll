def top_k(lst, k):
    sorted_list = []
    biggest = []
    while lst:
        largest = 0
        for i in lst:
            if i >= largest:
                largest = i
        lst.remove(largest)
        sorted_list.append(largest) # from biggest to smallest
    for j in range (k):
        biggest.append(sorted_list[j])
    return biggest
    pass
