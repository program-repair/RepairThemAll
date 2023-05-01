def sort_age(lst):
    # Fill in your code here
    result=[]
    for i in lst:
        result+=[i[::-1],]
    result.sort()
    result.reverse()
    ans=[]
    for i in result:
        ans+=[i[::-1],]
    return ans
