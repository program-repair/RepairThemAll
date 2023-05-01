def search(x, seq):
    for i in range(0,len(seq)):
        if x<seq[i]:
            return print(i)
        else:
            return print(len(seq))
