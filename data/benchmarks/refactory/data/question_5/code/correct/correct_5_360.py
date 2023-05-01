def sort_list(lst):
    if len(lst) < 2:
        return lst
    for i in range(len(lst)-1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min] > lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    lst.reverse()
    return lst   
def top_k(lst, k):
    ans = sort_list(lst)
    return ans[0:k]# Fill in your code here
    
