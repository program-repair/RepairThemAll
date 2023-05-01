def sort_age(lst):
    sorted_lst = []
    def oldest_in(lst):
        oldshit = lst[0]
        for i in lst:
            if oldshit[1] < i[1]:
                oldshit = i
        return oldshit
    while lst:
        old = oldest_in(lst)
        lst.remove(old)
        sorted_lst.append(old)
    return sorted_lst
