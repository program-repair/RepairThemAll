def sort_age(lst):
    swap = True
    while swap:
        swap = False
        for tag in range(len(lst)-1):
            if lst[tag][1] < lst[tag+1][1]:
                lst[tag], lst[tag+1] = lst[tag+1], lst[tag]
                swap = True
    return lst
