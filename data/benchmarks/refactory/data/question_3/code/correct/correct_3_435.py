def remove_extras(lst):
    
    def position(i,seq):
        n = len(seq)
        for j in range(n):
            if seq[j] == i:
                return j
    def helper(start,i):
        for k in lst[start:]:
            if k == i:
                n_pos = position(k,lst[start:])+ index +1
                print(k,n_pos)
                lst.pop(n_pos)
    for i in lst:
        index = position(i,lst)
        helper(index+1,i)

    return lst
