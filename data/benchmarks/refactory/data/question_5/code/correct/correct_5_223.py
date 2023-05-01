def top_k(lst, k):
    new_list = []
    while len(new_list) != k:
        largest = lst[0]
        for i in lst:
            if largest < i:
                largest = i
            else:
                continue
        new_list += [largest]
        lst.remove(largest)
    return new_list
            
