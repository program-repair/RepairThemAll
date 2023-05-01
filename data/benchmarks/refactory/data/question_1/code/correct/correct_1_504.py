def search(key, seq):
    lst = list(seq)
    n = len(lst)
    for i in range(n+1): #0,1,2,3 
        if i <= n-1 and key <= lst[i]:
            return i
    return n 
