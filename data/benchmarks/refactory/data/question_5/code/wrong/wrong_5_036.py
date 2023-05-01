def top_k(lst, k):
    if lst == []:
        return []
    elif k == 0:
        return lst
    else:
        final = []
        while lst:
            element = max(lst)
            final += [element,]
            lst.remove(element)
            if len(final) == k:
                break
        return final
