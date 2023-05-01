def sort_age(lst):
    new_lst=[lst[0],]
    for x in lst[1:]:
        if x[1] > new_lst[-1][1]:
            new_lst += [x,]
        else:
            count=0
            while count<len(new_lst):
                if x[1] > new_lst[count][1]:
                    count+=1
                    continue
                else:
                    new_lst = new_lst[0:count]+[x,]+new_lst[count:]
                    break
    return new_lst[::-1]
