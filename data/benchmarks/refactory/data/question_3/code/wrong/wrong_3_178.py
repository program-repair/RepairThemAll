def remove_extras(lst):
    # your code here
    n = 0
    while n < len(lst):
        lst = lst[n] + lst[n+1:].remove(lst[n])
        n = n + 1
    return lst
    pass
