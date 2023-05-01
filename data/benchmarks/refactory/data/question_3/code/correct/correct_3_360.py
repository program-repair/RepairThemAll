def remove_extras(lst):
    lsts = []
    for i in lst:
       if i not in lsts:
          lsts.append(i)
    return lsts

