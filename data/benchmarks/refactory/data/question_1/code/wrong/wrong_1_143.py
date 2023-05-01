def search(x, seq):
    n=[]
    seq = list(seq)
    a= seq.copy()
    d = 0
    if seq == ():
        return 0 
    for i in a:
        if i<x:
            n.append(i)
            seq.remove(i)
        elif i == x:
            n.append(i)
            n.append(x)
            n.extend(seq)
            break
        else:
            n.append(x)
            n.extend(seq)
            break
    count = list(enumerate(n))
    for b in count:
        d+=1
        if b[1] == x:
            return b[0]
        elif d==len(count):
            return d
