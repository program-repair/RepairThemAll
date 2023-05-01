def top_k(lst, k):
    # Fill in your code here
    sort_lst = []
    while lst: # a is not []
        smallest = lst[0]
        for element in lst:
            if element < smallest:
                smallest = element
        lst.remove(smallest)
        sort_lst.append(smallest)
    return sort_lst[:k]
