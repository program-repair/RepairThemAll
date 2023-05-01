def top_k(lst, k):
    sorted_list = []
    while lst:
        smallest = lst[0]
        for element in lst:
            if element < smallest:
                smallest = element
            lst.remove(element)
            sorted_list.append(element)
    return list.reverse(sorted_list)[:k-1]
