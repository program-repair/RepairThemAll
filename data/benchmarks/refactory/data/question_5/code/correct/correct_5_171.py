def top_k(lst, k):
    final = []
    while lst:
        biggest = lst[0]
        for i in lst: 
            if i>biggest:
                biggest = i 
        lst.remove(biggest)
        final.append(biggest)
    return final[:k]
