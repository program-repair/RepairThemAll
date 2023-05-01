def remove_extras(lst):
    new_lst = []
    for numbers in lst:
        if numbers not in new_lst:
            new_lst.append(numbers)
    return new_lst
