def search(x, seq):
    index = 0
    def helper(index):
        if not seq:
            return 0
        elif x <= seq[index]:
            return index
        else:
            if index + 1 >= len(seq):
                return index + 1
            else:
                return helper(index+1)
