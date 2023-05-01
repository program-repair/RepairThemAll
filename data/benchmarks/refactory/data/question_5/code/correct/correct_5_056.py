def top_k(lst, k):
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        else:
            mid = len(lst) // 2
            lst1 = merge_sort(lst[:mid])
            lst2 = merge_sort(lst[mid:])
            result = []
            
            while lst1 and lst2:
                if lst1[0] < lst2[0]:
                    result.append(lst2.pop(0))
                else:
                    result.append(lst1.pop(0))
            
            result.extend(lst1)
            result.extend(lst2)
            
            return result
    
    lst = merge_sort(lst)
    return lst[:k]
