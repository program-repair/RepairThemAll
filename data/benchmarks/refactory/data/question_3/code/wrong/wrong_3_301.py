def remove_extras(lst):
    n=len(lst)
    for i in lst:
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
    return lst
