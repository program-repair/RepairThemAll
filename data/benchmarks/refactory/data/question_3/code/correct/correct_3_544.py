def remove_extras(lst):
    dic = {}
    for e in lst:
        if e not in dic:
            dic[e] = 0
    return list(dic.keys())
