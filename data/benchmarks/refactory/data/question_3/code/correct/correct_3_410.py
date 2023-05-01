def remove_extras(lst):
    # your code here
    n = 0
    a = lst
    while n < len(a):
        if a[n] in a[n+1:]:
            b = a[n+1:]
            b.remove(a[n])
            a = a[:n+1] + b
        else:
            n = n + 1
    return a
