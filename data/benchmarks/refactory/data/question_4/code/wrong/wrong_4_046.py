def sort_age(lst):
    output = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] < smallsest[1]:
                smallest = i
        lst.remove(i)
        output.append(i)
    return output
