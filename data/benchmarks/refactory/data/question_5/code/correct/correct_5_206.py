def top_k(lst, k):
    i=0
    while i+1<len(lst):
        if lst[i]<lst[i+1]:
            lst.extend([lst[i]])
            lst.pop(i)
            i=0
        else:
            i+=1
    return lst[:k]
