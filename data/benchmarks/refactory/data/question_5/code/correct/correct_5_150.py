def top_k(lst, k):
    def merge_sort(lst):
        if len(lst) < 2:  # Base case!
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])  #sort left
        right = merge_sort(lst[mid:]) #sort right
        return merge(left, right)
    def merge(left, right):
        results = []
        while left and right:
            if left[0] > right[0]:
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        results.extend(left)
        results.extend(right)
        return results
    lst = merge_sort(lst)
    return lst[:k]
    
