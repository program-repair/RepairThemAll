def remove_extras(lst):
    lst.reverse()
    for elem in lst:
        while elem in lst[lst.index(elem)+1:]:
            lst.remove(elem)
            #reversing list to remove elements from the back.. I think?
    lst.reverse()
    new_lst = lst.copy()
    return new_lst

#Don't really understand the new list part. Does this mean they don't want me to modify
#the list that was input? Will making a shallow copy at the end suffice?
