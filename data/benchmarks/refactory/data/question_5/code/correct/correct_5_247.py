def bubble_sort(lst):
    swap = True
    while swap == True:
        swap = False
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
    return lst
    
def top_k(lst, k):
    lst = bubble_sort(lst)
    return lst[:k]
