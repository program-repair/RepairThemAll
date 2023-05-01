def sort_age(lst):
    output = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] < smallest[1]:
                smallest = i
        lst.remove(smallest)
        output.append(smallest)
    return output
