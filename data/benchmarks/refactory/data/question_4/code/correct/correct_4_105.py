def sort_age(lst):
    ages = list(i[1] for i in lst)
    
    for i in range(len(lst)):
        index_youngest = ages.index(max(ages))
        lst[i], lst[index_youngest] = lst[index_youngest], lst[i]
        ages[index_youngest] = min(ages) - 1
        ages[i], ages[index_youngest] = ages[index_youngest], ages[i]

        
    return lst
