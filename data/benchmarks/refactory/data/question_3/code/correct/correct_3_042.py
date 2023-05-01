def remove_extras(lst):
    if lst == []:
        return lst
    else:
        one = [lst[0],]
        for repeat in lst:
            if repeat not in one:
                one += [repeat,]
        return one
