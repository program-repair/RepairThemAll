def search(x,seq):
    for i in range(len(seq)):
        if len(seq) == 0:
            return 0
        elif x > max(seq):
            return len(seq)
        elif x > seq[i]:
            continue
        elif x <= seq[i]:
            break
        
    return i
