def top_k(lst, k):
    def sort(lst2):
        holder=[]
        if lst==[]:
            return []
        for x in lst:
            if holder==[]:
                holder=x
            elif x>holder:
                holder=x
        lst.remove(holder)
        return [holder]+sort(lst)
    counter=k
    final=[]
    new_lst=sort(list)
    while counter>0:
	    a=new_lst.pop(0)
	    final.append(a)
	    counter-=1
    return final
        
