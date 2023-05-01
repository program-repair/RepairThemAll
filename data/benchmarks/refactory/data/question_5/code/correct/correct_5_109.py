def top_k(lst, k):
    
    def sort(lst):

        new_lst=[]
        while lst:
            bigger=lst[0]
            for i in lst:
                if i>=bigger:
                    bigger=i 
            lst.remove(bigger)
            new_lst.append(bigger)

        return new_lst
        
    sorted_lst=sort(lst)
    return sorted_lst[:k]
                
            
    
