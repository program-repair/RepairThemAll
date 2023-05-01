def sort_age(lst):
    sorted = []
    while lst:
        youngest = lst[0]
        for elem in lst:
            if elem[1] < youngest[1]:
                youngest = elem
        print(youngest)
        lst.remove(youngest)
        sorted.append(youngest)
    return sorted
