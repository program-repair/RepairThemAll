def sort_age(lst):
    lst1=[]
    while lst:
        smallest=lst[0]
        for ele in lst:
            if ele[1]<smallest[1]:
                smallest=ele
        lst.remove(smallest)
        lst1.append(smallest)
    return lst1
