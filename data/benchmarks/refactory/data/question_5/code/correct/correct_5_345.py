def top_k(lst, k):
    new_list= selection_sort(lst)
    results= []
    for i in range(k):
        results.append(new_list.pop(0))
    return results
        
        

def selection_sort(lst):
    for idx in range(len(lst)):
        minimum=idx
        for i in range(len(lst)):
            if lst[i] < lst[minimum]:
                minimum=i
            lst[minimum], lst[idx]= lst[idx], lst[minimum]
    return lst
