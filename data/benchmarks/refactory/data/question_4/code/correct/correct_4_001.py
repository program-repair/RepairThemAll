def sort_age(lst):
    output = []
    for i in range(len(lst)):
        largest = max(lst, key=lambda p: p[1])
        lst.remove(largest)
        output.append(largest)
    return output
