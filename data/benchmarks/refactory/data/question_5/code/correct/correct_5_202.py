def top_k(lst, k):
    new = []
    counter = k
    while counter > 0:
        curr = 0
        for i in range(len(lst)):
            if lst[i] > lst[curr]:
                curr = i
        new.append(lst.pop(curr))
        counter -= 1
    return new
