def top_k(lst, k):
    if k<=0:
        return []
    else:
        maxi=max(lst)
        length=len(lst)
        for i in range(length):
            if lst[i]==maxi:
                pos=i
        new_list=lst.copy()
        new_list.pop(pos)
        return [maxi]+top_k(new_lst,k-1)
