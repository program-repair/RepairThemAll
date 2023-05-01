def search(x, seq):
    seq_len = len(seq)
    for i in range(seq_len):
        if x <= seq[i]: return i
    return seq_len
