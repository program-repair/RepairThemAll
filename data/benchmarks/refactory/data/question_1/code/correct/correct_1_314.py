def search(x, seq):
    count=0
    while count<len(seq):
        if x>seq[count]:
            count+=1
            continue
        else:
            return count
    return len(seq)
        
