def search(x, seq):
    for i, elem in enumerate(seq):
        if x < elem: 
            return i
        elif x == elem:
            return i
        elif i == len(seq)-1:
            return i+1
        elif seq == []:
            return 0
