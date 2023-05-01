def sort_age(lst):
    def helper(lol, lel):
        laugh = []
        while lol and lel:
            if lol[0][1] > lel[0][1]:
                laugh.append(lol.pop(0))
            else:
                laugh.append(right.pop(0))
        laugh.extend(lol)
        laugh.extend(right)
        return laugh
    if len(lst) < 2:
        return list(lst)
    centre = len(lst)//2
    left = sort_age(lst[:centre])
    right = sort_age(lst[centre:])
    return helper(left, right)
