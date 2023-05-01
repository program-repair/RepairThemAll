def sort_age(lst):
    if len(lst)<2:
        return lst
    while True:
        changed = False
        for i in range(len(lst)-1):
            if lst[i+1][1]>lst[i][1]:
                lst[i],lst[i+1] = lst[i+1], lst[i]
                changed = True
        if not changed:
            break
            
    return (lst)
