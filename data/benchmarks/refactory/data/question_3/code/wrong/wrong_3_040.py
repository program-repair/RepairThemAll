def remove_extras(lst):
    s = []
    for i in lst:
       if i not in lst:
          s.append(i)
    return s
    # your code here
    pass
