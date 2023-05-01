def sort_age(lst):
    result = []
    while lst !=[]:
        lowest = lst[0][1]
        index = 0
        for i in range(1,len(lst)):
            if lst[i][1]<lowest:
                index = i
                lowest = lst[i][1]
        result = result +[lst[index]]
        lst.pop[index]
    return result
            
