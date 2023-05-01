def merge_sort(lst):
    if len(lst) < 2:  
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)
    
def merge(left, right):
    results = []    
    while left and right:
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    results.extend(left)
    results.extend(right)
    return results  
def top_k(lst, k):
    result=merge_sort(lst)
    result.reverse()
    answer=[]
    for i in range(0,k):
        answer=answer+[result[i]]
    return answer
    pass
