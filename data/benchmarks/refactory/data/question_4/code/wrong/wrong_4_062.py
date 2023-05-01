def sort_age(lst):
    final=[]
    while lst:
        old=lst[0]
        for i in lst:
            if old[1]<i[1]:
                old=i
            final.append(old)
            lst.remove(old)
    return final
