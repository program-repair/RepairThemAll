def top_k(lst, k):
    descending_list=[]
    while lst:
        largest=lst[0]
        for i in lst:
            if i>largest:
                largest=i
        descending_list.append(largest)
        lst.remove(largest)
    return descending_list[:k]
