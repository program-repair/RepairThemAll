def top_k(lst, k):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
    #lst order done

    return lst[:k]
