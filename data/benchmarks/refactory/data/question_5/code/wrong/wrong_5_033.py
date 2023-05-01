def top_k(lst, k):
    final = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
            lst.remove(largest)
            final.append(largest)
        if len(final) == k:
            break
    return final
