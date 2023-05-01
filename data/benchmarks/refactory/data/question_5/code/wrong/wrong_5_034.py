def top_k(lst, k):
    final = []
    while lst:
        element = max(lst)
        final += [element,]
        lst.remove(element)
        if len(final) == k:
            break
    return final
