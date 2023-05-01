def search(x, seq):
    for i in range(len(sorted_seq)):
        if x <= sorted_seq[i]:
            return i
        else:
            return len(sorted_seq)

