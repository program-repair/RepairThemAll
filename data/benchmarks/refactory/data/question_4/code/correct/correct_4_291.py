def sort_age(lst):
    def get_age(person):
        return person[1]
    for i in range(len(lst)-1):
        for elem in lst[i+1:]:
            if get_age(elem) < get_age(lst[i]):
            #    lst[i], lst[lst.index(elem)] = lst[lst.index(elem)], lst[i]
            #above doesn't seem to change the list
                temp = lst.index(elem)
                lst[i], lst[temp] = lst[temp], lst[i]
    lst.reverse()
    return lst
