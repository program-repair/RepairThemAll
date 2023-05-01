def sort_age(lst):
    if len(lst) < 2:
        return lst
    for i in range(len(lst)-1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min][1] > lst[j][1]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    lst.reverse()
    return lst# Fill in your code here
    
