def remove_extras(lst):
    newlist = []
    for number in lst:
       if number not in newlist:
           newlist.append(number)
    return newlist
