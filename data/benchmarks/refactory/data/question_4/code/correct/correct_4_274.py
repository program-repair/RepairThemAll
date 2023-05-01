def sort_age(lst):
    if lst == []:
        return []
    else:
        agelist = [lst[0],]
        for i in range(1,len(lst)):
            if lst[i][1] > agelist[0][1]:
                agelist.insert(0, lst[i])
            elif lst[i][1] < agelist[len(agelist)-1][1]:
                agelist.insert(len(agelist), lst[i])
            else:
                for x in range(0,len(agelist)):
                    if agelist[x][1]> lst[i][1] > agelist[x+1][1]:
                        agelist.insert(x+1, lst[i])
                        break
        return agelist
    
