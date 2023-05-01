def sort_age(lst):
    youngest = lst[0][1]
    for item in lst:
        if item[1] < youngest:
            youngest = item[1]
            lst.remove(item)
            lst = [item,] + lst
            
    return lst

