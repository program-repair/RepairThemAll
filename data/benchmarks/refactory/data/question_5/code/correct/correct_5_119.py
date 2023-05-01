def top_k(lst, k):
    def sorter(lst):
        newlst = []
        while lst:
            current = lst[0]
            for element in lst:
                if element > current:
                    current = element
            newlst.append(current)
            lst.remove(current)
        return newlst
    return sorter(lst)[:k]
            
