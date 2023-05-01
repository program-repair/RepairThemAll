def sort_age(lst):
    # Fill in your code here
    a = []
    for i in lst:
        if a ==[]:
            a.append(i)
            continue
        else:
            for k in range(0,len(lst)):
                if i[1]>a[0][1]:
                    a.insert(0,i)
                    break
                elif a[-1][1]>i[1]:
                    a.insert(len(lst),i)
                    break
                elif i[1] > a[k+1][1] and i[1]<a[k][1]:
                    a.insert(k+1,i)
                    break
    return a
            
