def top_k(lst, k):
    def merge_lists(left,right):
        new = []
        while left and right:
            if left[0] >= right[0]:
                new.append(left.pop(0))
            else:
                new.append(right.pop(0))
        new.extend(left)
        new.extend(right)
        return new
                
    def binary_sort(lst):
        if len(lst) <2:
            return lst
        mid = len(lst)//2
        left = binary_sort(lst[:mid])
        right = binary_sort(lst[mid:])
        return merge_lists(left,right)
        
    new = binary_sort(lst)
    return new[:k]
