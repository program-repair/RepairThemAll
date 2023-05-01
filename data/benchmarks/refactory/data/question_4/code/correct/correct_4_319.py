def sort_age(lst):
    new=[]
    while lst:
        biggest=lst[0]
        for element in lst:
            if element[1]>biggest[1]: 
                biggest=element
                
        lst.remove(biggest)
        new.append(biggest)
    return new

