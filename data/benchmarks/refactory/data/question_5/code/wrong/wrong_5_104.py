def top_k(lst, k):
    counter=0
    new_lst=[]
    while counter<k:
        maxi=max(lst)
        new_lst.append(maxi)
        lst.remove(maxi)
        counter+=1
