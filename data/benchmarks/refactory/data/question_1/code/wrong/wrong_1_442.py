def search(x, seq):
    if seq==():
        return None
    for i in range(len(seq)):
        if x<=seq[i]:
            return i
    return i+1 
    
                
        
  
