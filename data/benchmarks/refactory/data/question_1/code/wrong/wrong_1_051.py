def search(x, seq):
    newseq = list(seq)
    sortlist = []
    if newseq[-1] < x:
        return len(newseq)
    while x not in sortlist and newseq:
        start = newseq[0]
        if x <= start:
            sortlist.append(x)
        else:
            sortlist.append(start)
            newseq.pop(0)
    sortlist.extend(newseq)
    for pos, elem in enumerate(sortlist):
        if elem == x:
            return pos
