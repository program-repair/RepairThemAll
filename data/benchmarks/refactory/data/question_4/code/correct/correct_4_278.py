def sort_age(lst):
    for start in range(len(lst)-1):
        oldest = start
        for i in range(start, len(lst)):
            if lst[i][1] > lst[oldest][1]:
                oldest = i
        lst[start], lst[oldest] = lst[oldest], lst[start]
    return list(lst)
