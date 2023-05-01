def sort_age(lst):
    ages=[]
    for j in lst:
        ages.append(j[1])
    ages=sort(ages)
    new_lst=[]
    for age in ages:
        for i in lst:
            if age==i[1]:
                new_lst.append(i)
    return new_lst
    
def sort(lst):
    age=[]
    while lst:
        largest=lst[0]
        for elem in lst:
            if elem > largest:
                largest = elem
        lst.remove(largest)
        age.append(largest)
    return age
    
