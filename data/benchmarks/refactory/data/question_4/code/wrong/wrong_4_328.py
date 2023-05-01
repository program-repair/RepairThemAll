def sort_age(lst):
    # Fill in your code here
    sorted = []
    while lst:
        oldest = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > oldest[1]:
                oldest = lst[i]
        sorted.append(lst.pop(i))
    return sorted
