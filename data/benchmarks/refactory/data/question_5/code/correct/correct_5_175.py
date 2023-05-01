def sort_no(lst):
    new = []
    while lst:
        Max = max(lst,key = lambda x : x)
        new.append(Max)
        lst.remove(Max)
    return new

def top_k(lst, k):
    Sorted = sort_no(lst)
    return Sorted[0:k]
