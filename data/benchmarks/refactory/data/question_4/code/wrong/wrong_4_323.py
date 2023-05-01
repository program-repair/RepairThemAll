def sort_age(lst):
    new_lst = lst
    newnew = [new_lst[0]]
    for i in new_lst:
        for j in range(len(newnew)):
            if i[1]>newnew[j][1]:
                newnew.insert(j+1,i)
            elif i[1]<newnew[j][1]:
                newnew.insert(j,i)
            return newnew
        return newnew
                
