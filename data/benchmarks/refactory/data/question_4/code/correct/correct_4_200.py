def sort_age(lst):
    new_lst = []
    for i in lst:
        if new_lst ==[]:
            new_lst+=[i]            
        else:
            pos=0
            for x in new_lst:
                if i[1]<x[1]:
                    pos+=1
                else:
                    continue
            new_lst[pos:pos]=[i]
    return new_lst
