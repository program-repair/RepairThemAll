def unique_day(day, possible_birthdays):
    def enumerate_tree(tree):
        def is_leaf(tree):
            return type(tree)!= tuple
        if tree == ():
            return ()
        elif is_leaf(tree):
            return (tree, )
        else:
            return enumerate_tree(tree[0]) + enumerate_tree(tree[1:])

    flat_tree = enumerate_tree(possible_birthdays)
    if flat_tree.count(day) > 1:
        return False
    
    return True
    
def unique_month(month, possible_birthdays):
    def enumerate_tree(tree):
        def is_leaf(tree):
            return type(tree)!= tuple
        if tree == ():
            return ()
        elif is_leaf(tree):
            return (tree, )
        else:
            return enumerate_tree(tree[0]) + enumerate_tree(tree[1:])

    flat_tree = enumerate_tree(possible_birthdays)

    if flat_tree.count(month) >1:
        return False
    return True
    
def contains_unique_day(month, possible_birthdays):
    tuppy = ()
    for x in possible_birthdays:
        if unique_day(x[1], possible_birthdays):
            tuppy += (x, )
            
    for y in tuppy:
        if y[0] == month:
            return True
    return False


