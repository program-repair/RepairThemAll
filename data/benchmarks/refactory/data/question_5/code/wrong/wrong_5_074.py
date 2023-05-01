def top_k(lst, k):
    results = []
    counter = 0
    while counter < k:
        for i in range(-len(lst),0):
            if lst[i] == max(lst):
                results.append(lst.pop(i))
                counter += 1
    return results
