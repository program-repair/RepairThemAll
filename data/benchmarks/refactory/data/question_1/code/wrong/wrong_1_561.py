def search(x, seq):
    if seq==[] or seq==():
        return 0
    elif x>=max(seq):
        return len(seq)
    else:
        for i in range(len(seq)):
            if x<=seq[i]:
                return i
                break
            else:
                continue
