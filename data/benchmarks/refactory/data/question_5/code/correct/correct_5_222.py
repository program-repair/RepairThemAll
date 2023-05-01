def top_k(lst, k):
    def sort(lst):
        sort = True
        while sort:
            sort = False
            for i in range(len(lst)-1):
                if lst[i] < lst[i+1]:
                    sort = True
                    lst[i], lst[i+1] = lst[i+1], lst[i]
        return lst
    lsts = sort(lst)
    return lsts[:k]
