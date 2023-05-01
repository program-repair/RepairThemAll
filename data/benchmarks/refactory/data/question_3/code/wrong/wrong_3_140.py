def remove_extras(lst):
    my_lst = []
    for i in lst:
        if i not in my_lst:
            my_lst.append(i)
        return my_lst

