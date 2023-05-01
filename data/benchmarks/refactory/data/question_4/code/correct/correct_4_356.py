def sort_age(lst):
    new_list=[]
    largest=0
    while lst:
        for i in lst:
            if i[1]>largest:
                largest = i[1]
                count=i
        new_list=new_list+[count]
        lst.remove(count)
        largest=0
    return new_list
