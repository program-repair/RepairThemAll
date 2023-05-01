def top_k(lst, k):
    def sortme(lst):
        sort=[]
        while lst:
            largest=lst[0]
            for i in lst:
                if i>largest:
                    largest=i
            lst.remove(largest)
            sort.append(largest)
        return sort
    return sortme(lst)[:k]
