def search(x, seq):
    for i in seq:
        if len(seq) == 0:
	        return 0
        elif x <= i:
            return seq.index(i)
        elif x > max(seq):
            return len(seq)
