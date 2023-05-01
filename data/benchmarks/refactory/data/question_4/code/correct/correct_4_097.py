def sort_age(lst):
    output = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        output.append(largest)
    return output
