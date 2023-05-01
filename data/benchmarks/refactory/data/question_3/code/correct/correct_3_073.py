def remove_extras(lst):
    sumx=[]
    for i in lst:
        if i not in sumx:
            sumx.append(i)
    return sumx
