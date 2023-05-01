def remove_extras(lst):
    i=1
    while True:
        if lst[i] in lst[:i]:
            del lst[i]
            continue
        
        if lst[i]==lst[-1]:
            break
        i=i+1
    return lst
