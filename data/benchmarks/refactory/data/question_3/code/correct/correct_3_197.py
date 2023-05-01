def remove_extras(lst):
    i=1
    if lst==[]: return lst
    
    while i!=len(lst):
        if lst[i] in lst[:i]:
            del lst[i]
            continue
        i+=1
    return lst
