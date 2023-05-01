def search(x, seq):
    if not seq:
        return 0
    elif x> seq[-1]:
        return len(seq)
    for i, elem in enumerate(seq):
        if x<=elem:
            break
    return i
