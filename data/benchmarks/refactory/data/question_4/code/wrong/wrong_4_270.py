def sort_age(lst):
    if len(lst) < 2:
        return lst
    midpoint = len(lst) // 2
    left = sort_age(lst[:midpoint])
    right = sort_age(lst[midpoint:])
    new_list = []
    while left and right:
        if left[0][1] < right[0][1]:
            new_list.append(right.pop(0))
        else:
            new_list.append(left.pop(0))
        new_list.extend(left)
        new_list.extend(right)
        return new_list
