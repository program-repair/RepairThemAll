def remove_extras(lst):
    # your code here
    out = []
    for ele in lst:
        if not ele in out:
            out.append(ele)
    return out
