def remove_extras(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] not in lst[:i]]
