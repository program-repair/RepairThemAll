def top_k(lst, k):
    new_lst=[]
    def bubble_sort(lst):
        swap = True
        while swap:
            swap = False
            for i in range(len(lst)-1):
                if lst[i]<lst[i+1]:
                    lst[i],lst[i+1]=lst[i+1],lst[i]
                    swap =True
        return lst
    sorted_lst = bubble_sort(lst)
    while k:
        new_lst.append(sorted_lst.pop(0))
        k-=1
    return new_lst
