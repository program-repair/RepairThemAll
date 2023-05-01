def search(x, seq):
    
    for i in range(len(seq)):
        if len(seq)==0:
            return 0
        elif x<=seq[i]:
            return i
        elif x>seq[len(seq)-1]:
            return len(seq)
        
        else:
            continue 
