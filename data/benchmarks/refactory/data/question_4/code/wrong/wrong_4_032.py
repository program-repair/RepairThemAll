def sort_age(lst):
    a=lst
    sort=[]
    while a:
        smallest=a[0]
        for element in a:
            if element[1]<smallest[1]:
                smallest=element
    a.remove(smallest)
    sort.append(smallest)
    return sort
