def search(x, seq):
    if seq == () or seq == []:
        return 0
    elif seq[-1] < x:
        return len(seq)
    newseq = list(seq)
    sortlist = []
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
