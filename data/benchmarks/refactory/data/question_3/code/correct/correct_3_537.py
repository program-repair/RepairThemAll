def remove_extras(lst):
    lst.reverse()
    for i in lst:
        n=len(lst)
        counter = 1
        number_of_appearance = 0
        while counter <= n:
            if i == lst[counter-1]:
                counter += 1
                number_of_appearance += 1
            else:
                counter += 1
        while number_of_appearance != 1:
            lst.remove(i)
            number_of_appearance -= 1
    lst.reverse()
    return lst
