def sort_age(lst):
    new_lst=[]
    new_lst.append(lst[0])
    for i in lst[1:]:
        for j in range(len(new_lst)):
            if i[1]>new_lst[j][1] and j==0:
                new_lst.insert(0,i)
            elif i[1]<new_lst[j][-1]:
                new_lst.insert(-1,i)
            elif i[1]>new_lst[j][1]:
                new_lst.insert(j,i)
    return new_lst
