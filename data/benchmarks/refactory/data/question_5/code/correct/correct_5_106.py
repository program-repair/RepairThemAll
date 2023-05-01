def top_k(lst, k):
    
    if lst == []:
        return lst
    def sorting(nlist):
        if nlist == []:
            return nlist
        lower = []
        higher = []
        plist = []
        pivot = nlist[0]
        for e in nlist:
            if e < pivot:
                lower.append(e)
            elif e == pivot:
                plist.append(e)
            elif e > pivot:
                higher.append(e)
        higher = sorting(higher)
        lower = sorting(lower)
        return lower + plist + higher
    
    sort_list = sorting(lst)
    sort_list = sort_list[::-1]
    
    return sort_list[:k]
