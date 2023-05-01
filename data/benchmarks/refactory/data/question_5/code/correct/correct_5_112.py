def top_k(lst,k):
    newlst=[]
    while lst:
        highest=lst[0] #first number
        for number in lst:
            if number>highest:
                highest=number
        for number in lst:
            if number==highest:
                newlst.append(number)
                lst.remove(number)
    return newlst[:k]
