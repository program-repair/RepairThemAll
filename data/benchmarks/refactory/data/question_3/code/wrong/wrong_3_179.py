def remove_extras(lst):
    # your code here
    n = 0
    while n < len(lst):
        if lst[n] in lst[n+1:]:
            lst = lst[:n+1] + lst[n+1:].remove(lst[n])
        n = n + 1
    return lst
