def get_largest(lst):
    for i in range (len(lst)-1):
        if lst[i]> lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
    
    return lst[-1]



def top_k(lst, k):
    result = []
    for i in range (len(lst)):
        if len(result) < k:
            largest = get_largest(lst)
            lst.remove(largest)
            result.append(largest)
    return result

