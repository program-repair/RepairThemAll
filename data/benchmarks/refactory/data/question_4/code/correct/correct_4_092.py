def sort_age(lst):
    # Fill in your code here
    new_lst = [('A',10000),('B',0)]
    for element in lst:
        age = element[1]
        for i in range(len(new_lst)):
            if age > new_lst[i][1]:
                new_lst.insert(i, element)
                break
    new_lst.remove(('A',10000))
    new_lst.remove(('B',0))
    return new_lst
