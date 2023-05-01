def sort_age(lst):
    final = []
    while lst:
        biggest = lst[0]
        for i in lst:
            if i[1] > biggest[1]:
                biggest = i
        lst.remove(biggest)
        final.append(biggest)
        print(final)
