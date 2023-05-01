def sort_age(lst):
    def merge(left,right):
        results = []
        while left and right:
            if left[0][1] > right[0][1]:
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        results.extend(left)
        results.extend(right)
        return results
    if len(lst) < 2:
        return lst
    mid = len(lst)//2
    left = sort_age(lst[:mid])
    right = sort_age(lst[mid:])
    return merge(left,right)
