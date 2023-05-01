def remove_extras(lst):
    #find the repeated index
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i] == lst[j] and i != j:
                a = lst[:j]+lst[n-j:]
            else:
                continue
    return a
