def top_k(lst, k):
    counter=0
    new_lst=[]
    while counter<k:
        new_lst.append(lst.remove(max(lst)))
