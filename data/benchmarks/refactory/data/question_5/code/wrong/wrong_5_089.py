def top_k(lst, k):
    newlist = []
    while lst:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
            else:
                continue
        lst.remove(biggest)
        if len(newlist) == k:
            break
        else:
            newlist.append(biggest)
        return newlist
