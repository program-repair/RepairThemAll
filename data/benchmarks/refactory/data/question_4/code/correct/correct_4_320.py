def sort_age(lst):
    for oldest in range(len(lst)-1):
        maxage = oldest
        for i in range(oldest,len(lst)):
            if int(lst[i][1]) > int(lst[maxage][1]):
                maxage = i
        lst[oldest], lst[maxage] = lst[maxage], lst[oldest]
    return lst
