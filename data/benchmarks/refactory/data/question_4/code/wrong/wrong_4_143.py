def sort_age(lst):
    males = []
    females = []
    for i in lst:
        if lst[0][0] == "M":
            males = males + [lst[0],]
        elif lst[0][0] == "F":
            females = females + [lst[0],]
    return merge_sort(males) + merge_sort(females)
    
def merge(left, right):
    results = []
    while left and right:
        if left[0][0] < right[0][0]:
            results.append(left,pop(0))
        else:
            results.append(right.pop(0))
    results.extend(left)
    results.extend(right)
    return results

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
