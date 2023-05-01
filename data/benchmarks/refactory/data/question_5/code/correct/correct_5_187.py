def top_k(lst, k):
    if k>len(lst):
        return None
    def newsort(lsts):
        l=[]
        while lsts:
            biggest=lsts[0]
            for element in lsts:
                if element>biggest:
                    biggest=element
            l.append(biggest)
            lsts.remove(biggest)
        return l
    newlist=newsort(lst)
    return newlist[0:k]
    
        
        
                
                
                    
