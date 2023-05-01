def sort_age(lst):
    final=[]
    while lst:
        old=lst[0]
        for i in lst:
            if old[1]<i[1]:
                old=i
            lst.remove(old)
            final.append(old)
    return final
