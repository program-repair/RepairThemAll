def search(x, seq):
    count=0
    for i in range (len(seq)):
        if x<=seq[i]:
            break
        count +=1
    return count
