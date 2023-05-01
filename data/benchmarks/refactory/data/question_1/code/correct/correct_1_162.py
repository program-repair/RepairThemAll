def search(x, seq):
    length = len(seq)
    if length == 0: return 0
    elif length == 1: return 0 if x < seq[0] else 1
    else:
        for i in range(length):
            if x <= seq[i]: return i
        return length # x is larger than everything in seq, so x goes to the end
