def sort_age(lst):
    for item in range(len(lst)):
        for test in range(len(lst)):
            if lst[test][1] < lst[item][1]:
                lst[test], lst[item] = lst[item], lst[test]
    return lst
