def sort_age(lst):
    n = len(lst)
    result = []
    while n != 0:
        test = []
        for counter in range(n):
            test.append(lst[counter][1])
        first = test(max)
        for counter in range(n):
            if lst[counter][1] == first:
                result.append(lst.pop(counter))
        n = len(lst)
    return result
        
