def sort_age(lst):
    lst.sort(key= lambda x: x[1], reverse = True)
    return lst
