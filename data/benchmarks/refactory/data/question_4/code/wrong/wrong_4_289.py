def sort_age(lst):
    new_list=[]
    largest=0
    while lst:
        for i in lst:
            if i[1]>largest:
                largest = i[1]
        new_list=new_list.append(i)
        lst.remove(i)
    return new_list
