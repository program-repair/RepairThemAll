def top_k(lst, k):
    new_lst = []
    while lst:
        maxi = lst[0]
        for item in lst:
            if item > maxi:
                maxi = item
        new_lst.append(maxi)
        lst.remove(maxi)
    return new_lst[0:k]# Fill in your code here
