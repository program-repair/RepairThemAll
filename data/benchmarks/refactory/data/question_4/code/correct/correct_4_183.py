# person = ("M",30)
#people list = [("M",30),("F",23)]

def sort_age(lst):
    
    if len(lst) <= 1:
        return lst

    else:
        newlist = []
        biggest = lst[0]
        for i in lst[1:]:
            if biggest[1] > i[1]:
                continue
            else:
                biggest = i
                continue
            
        newlist += [biggest]
    
        lst.remove(biggest)
    
        return newlist + sort_age(lst)


