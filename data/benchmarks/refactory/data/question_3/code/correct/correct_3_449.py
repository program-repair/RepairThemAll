def remove_extras(mylist):
    newlist=[]
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist

