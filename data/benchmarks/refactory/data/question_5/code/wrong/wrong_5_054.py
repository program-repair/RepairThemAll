def top_k(lst, k):
    count = 0
    op = []
    big = lst[0]
    while count < k:
        op += [max(lst)]
        count += 1
    return op
            
    
