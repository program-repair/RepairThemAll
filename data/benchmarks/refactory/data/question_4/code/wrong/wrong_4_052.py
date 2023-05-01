def sort_age(lst):
    newlst=[]
    while lst:
        oldest = lst[0][1] #first age
        for person in lst:
            if person[1]>oldest:
                oldest=person[1]
                newlst.append(person)
                lst.remove(person)
        newlst.append(lst[0])
        lst.remove(lst[0])
    return newlst
