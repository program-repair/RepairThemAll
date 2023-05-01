
def biggest(lst):
    big=lst[0]
    for i in range (len(lst)):
        if lst[i]>big:
            big=lst[i]
        else:
            continue
    return big
    
def top_k(lst, k):
    l=len(lst)
    new_list=[]
    for i in range (l):
        new_list.append(biggest(lst))
        lst.remove(biggest(lst))
    return new_list[:k]

