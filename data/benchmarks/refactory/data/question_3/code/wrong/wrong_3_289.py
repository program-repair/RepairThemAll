def remove_extras(lst):
    new_list=[]
    for i in range(len(lst)):
        judge=0
        for j in range(i):
            if lst[i]==lst[j]:
                judge=1
        if judge==0:
            new_list+=[lst[i],]
    return new_lst
    # your code here
    pass
