def sort_age(lst):
    result = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element[1] > biggest[1]:
                biggest = element
        lst.remove(biggest)
        result.append(biggest)
    return result
