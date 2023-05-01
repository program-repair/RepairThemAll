def top_k(lst, k):
    lst=sort_list(lst)
    while len(lst)>k:
        lst.pop(-1)
    return lst


def sort_list(lst):
    sort=[]
    while lst:
        largest=lst[0]
        for i in lst:
            if i>largest:
                largest=i
        lst.remove(largest)   #1.indentation: under while loop
        sort+=[largest]
    return sort

#1. find the largest first, then remove it from the lst, 
#then append the sort 
