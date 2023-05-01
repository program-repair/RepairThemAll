def top_k(lst, k):
    sort = []
    while lst:
        big = max(lst)
        sort.append(big)
        lst.remove(big)
    
    output = [n for n in lst if lst.index(n) < k]
    return output
