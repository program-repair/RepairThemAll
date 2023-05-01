def search(x, seq):
    new_seq=[]
    position=0
    for i in range(len(seq)):
        if x>seq[i]:
            position+=1
    return position
