def remove_extras(lst):
    
    def position(i):
        n = len(lst)
        for j in range(n):
            if lst[j] == i:
                return j
    def helper(start,i):
        for k in lst[start:]:
            if k == i:
                lst.remove(k)
        else:
            pass
        
    for i in lst:
        index = position(i)
        helper(index+1,i)
    return lst
