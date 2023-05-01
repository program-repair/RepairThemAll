def remove_extras(lst):
    new_list=[]
    for value in lst:
       if value not in new_list:
          new_list.append(value)
    return new_list
    
