def top_k(lst, num):
    def insertion_sort(lst):
        for i in range(len(lst)):
            if i == 0: continue
            else:
                while i > 0:
                    if lst[i] < lst[i-1]:
                        lst[i], lst[i-1] = lst[i-1], lst[i]
                        i -= 1
                    else: i = 0

    insertion_sort(lst)
    lst.reverse()
    
    score, result = -1, []
    for i in lst:
        if i == score:
            result += (i,)
        elif len(result) >= num: break
        else:
            result += (i,)
            score = i
    return result
