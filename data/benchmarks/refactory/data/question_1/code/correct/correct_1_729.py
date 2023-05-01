def search(x, seq):
    if seq == [] or seq ==():
        return 0
    elif x > seq[ len(seq)- 1]:
        return len(seq)    
    elif x < seq[0]:
        return 0
    else:
        for i in range(len(seq)):
            if x >= seq[i] and x <= seq[i+1]:
                return i+1
