def sort_age(lst):
    slist = []
    while lst:
        elder = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > elder[1]:
                elder = lst[i]
            else:
                continue
        slist.append(elder)
        lst.remove(elder)
    return slist
    
