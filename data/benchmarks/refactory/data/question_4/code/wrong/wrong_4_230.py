def sort_age(lst):
    oldest = lst[0][1]
    for item in lst:
        if item[1] > oldest:
            oldest = item[1]
            lst.remove(item)
            lst = [item,] + lst
            
    return lst

