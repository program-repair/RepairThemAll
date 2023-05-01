def sort_age(lst):
    def cmp(a,b):
        if a[1] >= b[1]:
            return True
        else:
            return False
        
    while True:
        sorted = True
        for i in range(len(lst)-1):
            if not cmp(lst[i],lst[i+1]):
                lst[i],lst[i+1]=lst[i+1],lst[i]
                sorted = False
        if sorted==True:
            break

    return lst
