def sort_age(lst):
    newnew = []
    for i in lst:
        for j in range(len(newnew)):
            if i[1]>newnew[j][1]:
                newnew.insert(j+1,i)
            elif i[1]<newnew[j][1]:
                newnew.insert(j,i)
            else:
                newnew.append(i)
            return newnew
        return newnew
                
