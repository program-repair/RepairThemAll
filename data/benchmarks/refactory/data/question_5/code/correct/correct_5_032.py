
def top_k(lst, k):
    # Fill in your code here
 
    result = []
    while lst:
        minimum = lst[0]  # arbitrary number in list 
        for x in lst: 
            if x > minimum:
                minimum = x
        result.append(minimum)
        lst.remove(minimum) 
    return result[:k]
