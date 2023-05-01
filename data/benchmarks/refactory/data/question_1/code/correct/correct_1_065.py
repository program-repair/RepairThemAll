def search(x, seq):
    if len(seq) == 0:    #if there is nothing in the sequence, put it as the first part of the column
        return 0
    else:
        for i in range(len(seq)):
            if x > seq[-1]:  #if the digit x is greater than the greatest number in the sequence, return the number of elements in the sequence
                return len(seq)
            elif x <= seq[i]: #to return the number when x is smaller of equals to the i in the loop
                return i
            else:
                continue #goes into a loop until it finds the number that matches the previous answer.
