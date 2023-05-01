def search(x, seq):
    for position in range(len(seq)):
        if x < seq[position] or x == seq[position]:
            return position
    return len(seq)
