def search(x, seq):
    if seq == () or seq == []:
        return 0
    for i in range (0, len(seq)):
        if x <= seq[i]:
           pos = i
           return pos
        if x > seq[len(seq)-1]:
           return len(seq)
        
