def sort_age(lst):
    biggest = lst[0][1]
    for i in range(len(lst)):
        if lst[0][1]<lst[i][1]:
            biggest = lst[i][1]
            continue
        else:
            biggest = lst[0][1]
    return [(biggest),] + sort_age(lst[1:len(lst)])         
    pass
