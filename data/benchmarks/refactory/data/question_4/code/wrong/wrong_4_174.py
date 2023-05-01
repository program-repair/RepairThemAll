def sort_age(lst):
    sort=[]
    while lst:
        smallest = lst[0][1]
        for i in range (len(lst)):
            if lst[i][1] < smallest:
                smallest = lst[i][1]
        lst.remove(smallest)
        sort.append(smallest)
        sort.reverse(smallest)
        return sort
