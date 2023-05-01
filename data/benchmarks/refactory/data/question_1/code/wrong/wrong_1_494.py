def search(x, seq):
    if seq == () or []:
        return None
    else:
        for i, elem in enumerate (seq):
            if x<=elem:
                return i
            elif x>seq[-1]:
                return len(seq)
