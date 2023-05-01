def sort_age(lst):
    if len(lst) == 1:
        return lst
    else:
        new_list = []
        while lst:
            minimum = lst[0]
            for i in lst:
                if i[1] < minimum[1]:
                    minimum = x
            new_list.append(minimum)
            lst.remove(minimum)
        return new_list
