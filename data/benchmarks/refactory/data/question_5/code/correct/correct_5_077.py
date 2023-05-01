def top_k(lst, k):
    def quick_sort(lst):
        def cmp(a,b):
            if a > b:
                return True
            else:
                return False    
    
        if len(lst)==0:
            return []
    
        lst0=[]
        lst1=[]
    
        partition = lst[0]
    
        for item in lst[1:]:
            if cmp(item,partition):
                lst0.append(item)
            else:
                lst1.append(item)
    
        return quick_sort(lst0)+[partition]+quick_sort(lst1)
    
    return quick_sort(lst)[:k]
