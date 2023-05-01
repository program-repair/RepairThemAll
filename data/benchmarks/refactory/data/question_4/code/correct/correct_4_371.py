def sort_age(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j][1] > a[j-1][1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a
