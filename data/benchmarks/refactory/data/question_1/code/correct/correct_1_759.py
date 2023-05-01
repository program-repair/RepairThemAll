def search(x, seq):
    if seq==[] or seq==():
        return 0
    else:
        for i in range(len(seq)):
            if i <range(len(seq))[-1]:
                if x<=seq[i]:
                    return i
                    break
                else:
                    continue
            else:
                if x<=seq[i]:
                    return i
                    break
                else:
                    return len(seq)
