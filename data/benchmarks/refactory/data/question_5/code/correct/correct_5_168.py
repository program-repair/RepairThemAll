def top_k(lst, k):
    new_lst = []
    if k == 0 or lst == []:
        return []
    else:
        while k > 0:
            new_lst.append(max(lst))
            lst.remove(new_lst[-1])
            k -= 1
        return new_lst
