def sort_age(lst):
    if len(lst)==1:
        return lst
    else:
        temp=lst[0][1]
        count=0
        for i in range(len(lst)):
            if lst[i][1]>temp:
                temp=lst[i][1]
                count=i
        result=[lst[count],]
        pop=lst.pop(count)
        return result+sort_age(lst)
    # Fill in your code here
    pass
