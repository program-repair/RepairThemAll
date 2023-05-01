def remove_extras(lst):
    new = []
    if lst == []:
        return lst 
    else:
        for i in lst:
            if i in new:
                continue 
            else:
                new.append(i)
    return new
