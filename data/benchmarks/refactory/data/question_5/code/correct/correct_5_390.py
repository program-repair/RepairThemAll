def top_k(lst, k):
    def sort(lst):
        if lst==[] or len(lst)==1:
            return lst
        else:
            temp=lst[0]
            count=0
            for i in range(len(lst)):
                if lst[i]>temp:
                    temp=lst[i]
                    count=i
            pop=lst.pop(count)
            return [temp,]+sort(lst)
    lst=sort(lst)
    return lst[:k]
    # Fill in your code here
    pass
