def top_k(lst, k):
    result = []
    while lst:
        biggest = lst[0]
        for elem in lst:
            if elem > biggest:
                biggest = elem
        lst.remove(biggest)
        result.append(biggest)
    
    return result[:k]

    # Fill in your code here
    pass


