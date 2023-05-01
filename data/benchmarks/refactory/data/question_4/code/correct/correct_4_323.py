def sort_age(lst):
    newlst=[]
    lstages=[i[1] for i in lst]
    while lst:
        for i in lst:
            if i[1] == max(lstages):
                newlst+=[i]
                lst.remove(i)
                lstages.remove(i[1])
    return newlst
