def sort_age(lst):
    newlst=[]
    while lst:
        oldest = lst[0][1] #first age
        for person in lst:
            if person[1]>oldest:
                oldest=person[1]
        for person in lst:
            if person[1]==oldest:
                newlst.append(person)
                lst.remove(person)            
    return newlst
