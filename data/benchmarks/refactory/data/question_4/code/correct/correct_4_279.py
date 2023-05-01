def sort_age(lst):
    if len(lst)<2:
        return lst
    def merge(lst1, lst2, key):
        r=[]
        while lst1!=[] and lst2!=[]:
            if key(lst1[0])>key(lst2[0]):
                r.append(lst1[0])
                lst1.remove(lst1[0])
            else:
                r.append(lst2[0])
                lst2.remove(lst2[0])
        r.extend(lst1)
        r.extend(lst2)
        return r
    m=len(lst)//2
    key=lambda tup: tup[1]
    return merge(sort_age(lst[:m]), sort_age(lst[m:]), key)
