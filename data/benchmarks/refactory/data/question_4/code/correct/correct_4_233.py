def sort_age(lst):
    for i in range(len(lst)-1):
        for ele in range(i+1, len(lst)):
            if lst[i][1] < lst[ele][1]:
                lst[i], lst[ele] = lst[ele], lst[i]
    return lst
   
   
   
