def top_k(lst, k):
    # Fill in your code here
    def ins_sort(a):
        i = 1
        while i < len(a):
            j = i
            while j>0 and a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                j-=1
            i+=1
        return a[::-1]
        
    lst_sorted = ins_sort(lst)
    
    return lst_sorted[:k]
