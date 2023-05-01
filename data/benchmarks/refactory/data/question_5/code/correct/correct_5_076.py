def top_k(lst, k):
    """
    sorts list in descending order
    returns the greatest k number of values (last k elements)
    """
    def merge(left,right):
        merged = []
        while left and right:
            if left[0] > right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        return merged + left + right
    def merge_sort(lst):
        if len(lst) == 1:
            return lst
        if len(lst) == 2:
            if lst[0] > lst[1]:
                return lst
            else:
                return lst[::-1] #reverse list
        else:
            a = len(lst)//2
            return merge(merge_sort(lst[:a]),merge_sort(lst[a:]))
    lst = merge_sort(lst)
    return lst[:k]
        
