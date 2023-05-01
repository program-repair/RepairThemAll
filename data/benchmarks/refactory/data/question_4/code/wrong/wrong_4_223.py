def sort_age(lst):
    a=[]
    while lst:
        for i in lst:
            if i==max(lst):
                a.append(i)
    return a
