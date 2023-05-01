def search(x, seq):
    count=0
    while count<len(seq):
        if x>seq[count]:
            count+=1
            continue
        else:
            if count!=0:
                return count-1
            else:
                return 0
    return len(seq)
        
