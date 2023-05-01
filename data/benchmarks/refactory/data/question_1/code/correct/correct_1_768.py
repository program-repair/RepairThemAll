
def search(x, seq):
    if seq==[] or seq==():
        return 0
    elif x<seq[0]:
        return 0
    elif x>seq[-1]:
        return len(seq)
    for i in range(len(seq)-1):
        if x>seq[i] and x<=seq[i+1]:
            return i+1
