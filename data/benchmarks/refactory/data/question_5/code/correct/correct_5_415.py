def top_k(lst, k):
    new_lst = []
    counter = 1
    while counter <= k:
        highest = lst[0]  # arbitrary number in list 
        for x in lst: 
            if x > highest:
                highest = x
        new_lst.append(highest)
        lst.remove(highest)
        counter +=1
        
    return new_lst
