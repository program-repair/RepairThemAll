def biggest(lst):
    big=lst[0]
    for i in range (len(lst)):
        if lst[i][1]>big[1]:
            big=lst[i]
        else:
            continue
    return big
    
def sort_age(lst):
    sorted_lst=[]
    while lst:
        sorted_lst.append(biggest(lst))
        lst.remove(biggest(lst))
    return sorted_lst
