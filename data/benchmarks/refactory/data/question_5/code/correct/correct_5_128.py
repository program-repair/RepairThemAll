def top_k(lst, k):
    def mergesort(lst):
        if len(lst) > 1:
            mid = len(lst)//2
            leftlst = lst[:mid]
            rightlst = lst[mid:]
            mergesort(leftlst)
            mergesort(rightlst)
            i = 0
            j = 0
            k = 0
            while i < len(leftlst) and j < len(rightlst):
                if leftlst[i] >= rightlst[j]:
                    lst[k] = leftlst[i]
                    i = i + 1
                else:
                    lst[k] = rightlst[j]
                    j = j + 1
                k = k + 1
            while i < len(leftlst):
                lst[k] = leftlst[i]
                i = i + 1
                k = k + 1
            while j < len(rightlst):
                lst[k] = rightlst[j]
                j = j + 1
                k = k + 1
    mergesort(lst)
    return lst[:k]
