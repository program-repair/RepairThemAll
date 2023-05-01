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
    final = []
    if n ==0:
        return []
    elif n ==1:
        return lst
    else:
        final = [largest_age(lst)]
        lst.remove(largest_age(lst))
        final = final + sort_age(lst)
        return final

