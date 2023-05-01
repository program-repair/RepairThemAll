def sort_age(lst):
    final = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] < smallest[1]:
                smallest = i
        lst.remove(smallest)
        final.append(smallest)
    print(lst)
