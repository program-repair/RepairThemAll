def sort_age(lst):
    final = []
    temp = 0
    while lst:
        biggest = lst[0][1]
        for i in lst:
            if i[1]>=biggest:
                biggest = i[1]
                temp = i 
        lst.remove(temp)
        final.append(temp)
    return final

