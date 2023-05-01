def top_k(lst, k):
    values = []
    while len(values) < k:
        for item in lst:
          greatest = lst[0]
          if item > greatest:
            greatest = item
        lst.remove(greatest)
        values.append(greatest)
        
    return values

