def sort_age(lst):
    if len(lst)== 0:
        return []
    def rank(lyst):
        if len(lyst)==1:
            return list(lyst)
        else:
            a = max(lyst)
            lyst.remove(a)
            return [a]+ rank(lyst)
    a = []
    b = []
    n = len(lst)
    for psn in lst:
        age = psn[1]
        a += [age]
        print(a)
    c = rank(a)
    for age in c:
        for psn in lst:
            if age == psn[1]:
                b += [psn]
            else:
                continue
    return b
