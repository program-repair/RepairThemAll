def top_k(lst, k):
    newlist = []
    while len(newlist) < k:
        newlist += [max(lst)]
        for i in range(len(lst)):
            if i == max(lst):
                print(i)
                break
        del lst[i]
    return newlist
