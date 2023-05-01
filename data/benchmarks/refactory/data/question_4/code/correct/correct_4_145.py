#def sort_age(lst):
#    lst.sort(key=lambda x: x[1],reverse=True)
#    return lst

def sort_age(lst):
    a=lst
    sort=[]
    while a:
        largest=a[0]
        for i in a:
            if i[1]>largest[1]:
                largest=i
        a.remove(largest)   #1.indentation!
        sort.append(largest)
    return sort

#1.it's same indentation as for loop,
    #that is, we only start removing when we find the largest 
