def sort_age(lst):
    sorted_age = []
    while lst:
        oldest = lst[0]
        for i in lst:
            if i[1] > oldest[1]:
                oldest = i
        sorted_age.append(oldest)
        lst.remove(oldest)
    return sorted_age
