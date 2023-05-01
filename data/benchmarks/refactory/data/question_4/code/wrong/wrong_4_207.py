def merge(one,two):
    new_tup = []
    while left and right:
        if one[0][1] < two[0][1]:
            new_tup.append(one.pop(0))
        else:
            new_tup.append(two.pop(0))
    return new_tup

def sort_age(lst):
    n = len(lst)
    if n <2:
        return lst
    left = lst[:n/2]
    right = lst[n/2:]
    return merge(left,right)
    
