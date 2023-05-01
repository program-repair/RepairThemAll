def remove_extras(lst):
    # your code here
    l=[]
    for i in lst:
        if i not in l:
            l.append(i)
    return l
