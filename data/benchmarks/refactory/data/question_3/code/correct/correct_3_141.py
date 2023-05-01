def remove_extras(lst):
    new = []
    for num in lst:
        if num in new:
            continue
        new.append(num)
    return new
        
