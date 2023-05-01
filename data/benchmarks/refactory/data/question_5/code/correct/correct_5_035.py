def top_k(lst, k):
    result = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i>largest:
                largest = i
        lst.remove(largest)
        result.append(largest)
    return result[:k]
        
        
        
        
        
        
#def sort_age(lst):
   # sort = []
   # while lst:
     #   oldest = lst[0]
     #   for person in lst:
         #   if person[1] >= oldest[1]:
            #    oldest = person
       # lst.remove(oldest)
      #  sort.append(oldest)
   # return sort
