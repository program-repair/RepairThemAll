def top_k(lst, k):
    new = []
    i = 1
    while i <= k:
        element = find_largest(lst)
        new.append(element)
        lst.remove(element)
        i = i+1
    return new

def find_largest(lst):
    largest = lst[0]
    for element in lst:
        if element > largest:
            largest = element
    return largest
