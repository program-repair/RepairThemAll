def search(x, seq):
    
    for i in range(len(seq)):
        if x<=seq[i]:
            return i
        elif x>seq[len(seq)]:
            return len(seq)
        elif len(seq)==0:
            return 0
        else:
            continue 
