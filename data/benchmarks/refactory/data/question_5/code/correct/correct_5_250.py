
def top_k(lst, k):
    x = []
    for i in range(k):
        a = 0
        for ele in lst:
            if ele >= a:
                a = ele
        lst.remove(a)
        x.append(a)
    return x
