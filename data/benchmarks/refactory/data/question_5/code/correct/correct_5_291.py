def top_k(lst, k):
    newlist = []
    while len(newlist)<k:
        newlist.append(max(lst))
        lst.remove(max(lst))
    return newlist
