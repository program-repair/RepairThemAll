def sort_age(lst):
    # Fill in your code here
    A = map(lambda x:x[1],lst)
    a = []
    counter =0
    while counter<len(lst):
        for i in A:
            if i>a[0]:
                a = i.extend(a)
            elif i<a[-1]:
                a = a.extend(i)
        counter += 1
    
    b = []
    for i in a:
        for y in lst:
            if y[1] ==i:
                b.append(y)
    return b
        
    
        
