def sort_age(lst):
        new=[]
        while lst !=[]:
            big=lst[0]
            for i in lst:
                if i>big:
                    big=i
            lst.remove(big)
            new.append(big)
        return new
def top_k(lst, k):
    return sort_age(lst)[:k]
    pass
