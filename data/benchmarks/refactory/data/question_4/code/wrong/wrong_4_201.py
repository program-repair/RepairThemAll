def sort_age(lst):
    agelist = [lst[0],]
    for i in lst:
        if i[1] > agelist[0][1]:
            agelist.insert(0, i)
        elif i[1] < agelist[len(agelist)-1][1]:
            agelist.insert(len(agelist), i)
        else:
            for x in range(0,len(agelist)):
                if agelist[x][1]< i[1] < agelist[x+1][1]:
                    agelist.insert(x+1, i)
    return agelist
