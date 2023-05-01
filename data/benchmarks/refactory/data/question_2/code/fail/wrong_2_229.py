def unique_day(day, possible_birthdays):
    flat_possible_birthdays=enumerate_tree(possible_birthdays)
    if flat_possible_birthdays.count(day) == 1:
        return True
    else:
        return False

def enumerate_tree(tree):
    if tree == ():
        return ()
    elif is_leaf(tree):
        return (tree,)
    else:
        return enumerate_tree(tree[0])+enumerate_tree(tree[1:])
def is_leaf(item):
    return type(item) != tuple

def unique_month(month, possible_birthdays):
    flat_possible_birthdays=enumerate_tree(possible_birthdays)
    if flat_possible_birthdays.count(month) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for each_day_in_month in filter(lambda x: x[0] == month, possible_birthdays):
        if unique_day(each_day_in_month[1], possible_birthdays) == True:
            res = True
        else:
            res = False
    return res

def filter(pred,seq):
    if seq ==():
        return ()
    elif pred(seq[0]):
        return (seq[0],)+filter(pred,seq[1:])
    else:
        return filter(pred,seq[1:])
