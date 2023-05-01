def remove_extras(lst):
    removed = []
    for e in lst:
       if (e in lst) and (e not in removed):
          removed.append(e)
    return removed
