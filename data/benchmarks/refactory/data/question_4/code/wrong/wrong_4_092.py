def sort_age(lst):
    answer = []
    for i in range(0,len(lst),-1):
        biggest = lst[i]
        for a in range(i):
            if lst[a][1] > biggest[1]:
                biggest = lst[a]
        answer += biggest        
    return answer
