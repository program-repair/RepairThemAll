
def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
        elif x >= max(seq):
            return len(seq) 
        else:
            continue 
