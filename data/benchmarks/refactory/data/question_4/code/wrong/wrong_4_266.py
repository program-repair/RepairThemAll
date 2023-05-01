def sort_age(lst):
    while lst:
        smallest = lst[0][1]
        for x in lst:
            if x[1] < smallest:
                smallest = x
        lst.remove(smallest)
        sort.append(smallest)
        return lst
