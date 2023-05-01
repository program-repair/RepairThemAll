def sort_age(lst):
    ans = []
    while lst:
        biggest = lst[0]
        for elem in lst:
            if elem[1] > biggest[1]:
                biggest = elem
        lst.remove(biggest)
        ans.append(biggest)
    
    return ans
    
    
