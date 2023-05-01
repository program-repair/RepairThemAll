def top_k(lst, k):
    def pos(seq,i):
        n = len(seq)
        for j in range(n):
            if seq[j] == i:
                return j
    def largest(seq):
        largest = seq[0]
        for i in seq:
            if i > largest:
                largest = i
        return pos(seq,largest)
    n_list =[]
    if k ==1:
        return [lst[largest(lst)]]
    elif lst == [] or k==0:
        return []
    else: 
        z = lst.pop(largest(lst))
        n_list = [z]+ top_k(lst, k-1)
        return n_list 
    
    
    # Fill in your code here
    pass
