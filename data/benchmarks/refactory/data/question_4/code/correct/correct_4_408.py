def sort_age(lst):
    result = []
    while lst:
        oldest = lst[0]
        for people in lst:
            if people[1] > oldest[1]:
                oldest = people
        lst.remove(oldest)
        result += (oldest,)
    return result
