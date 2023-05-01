def top_k(lst, k):
    if lst == [] or k == 0:
        return []
    else:
        final = []
        while lst:
            element = max(lst)
            final += [element,]
            lst.remove(element)
            if len(final) == k:
                break
        return final
