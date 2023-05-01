def top_k(lst, k):
    final = []
    while len(final) != k:
        a = max(lst)
        final.append(a)
        lst.remove(a)
    return final
        
