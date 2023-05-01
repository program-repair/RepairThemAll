def sort_age(lst):
    def age(i):
        return i[1]
        
    def position(seq, ele):
        n = len(seq)
        for i in range(n):
            if seq[i] == ele:
                return i
                
    def largest_age(seq):
        largest = age(seq[0])
        largest_pos = 0
        for i in seq:
            if age(i) > largest:
                largest = age(i)
                largest_pos = position(seq,i)
        return seq[largest_pos]
    n = len(lst)
    if n ==0:
        return []
    elif n ==1:
        return lst
    else:
        return [largest_age(lst)]+[sort_age(lst[1:])]
        
        
    # Fill in your code here
    pass
