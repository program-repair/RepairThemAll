def remove_extras(lst):
    for element in lst:
        for count in lst:
            if count +2 > len(lst):
                return lst
            elif lst[count+1] == element:
                lst.remove(element)
                continue
            return lst
        
        
        
