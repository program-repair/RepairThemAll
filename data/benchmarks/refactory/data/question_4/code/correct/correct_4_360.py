def sort_age(lst):
    result=[]
    while lst:
        minimum=lst[0]
        for i in lst:
            if i[1]<minimum[1]:
                minimum=i
        result.append(minimum)
        lst.remove(minimum)
    return result[::-1]
    
