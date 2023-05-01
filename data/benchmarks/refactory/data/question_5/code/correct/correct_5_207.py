def top_k(lst, k):
    a = lst
    sort=[]
    while a:
        smallest = a[0]
        for element in a:
            if element<smallest:
                smallest = element
        a.remove(smallest)
        sort.append(smallest)
    sort.reverse()
    return sort[0:k]
