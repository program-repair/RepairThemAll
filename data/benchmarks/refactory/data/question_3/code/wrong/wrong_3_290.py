def remove_extras(lst):
    new_list=[]
    for e in lst:
        if not is_same(element,new_list):
            new_list.append(element)
        else:
            continue
    return new_list
    
def is_same(test,lst):
    for e in lst:
        if e == test:
            return True
        else:
            continue
    return False
    
