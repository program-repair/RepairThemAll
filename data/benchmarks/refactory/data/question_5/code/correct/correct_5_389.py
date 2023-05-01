def sort(lst):
    if lst==[]:
        return []
    new_lst=[lst[0],]
    for x in lst[1:]:
        if x > new_lst[-1]:
            new_lst += [x,]
        else:
            count=0
            while count<len(new_lst):
                if x > new_lst[count]:
                    count+=1
                    continue
                else:
                    new_lst = new_lst[0:count]+[x,]+new_lst[count:]
                    break
    return new_lst[::-1]

def top_k(lst, k):
    return sort(lst)[0:k]
