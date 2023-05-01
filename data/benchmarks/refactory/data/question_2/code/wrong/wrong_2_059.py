def unique_day(day, pb):
    n = len(pb)
    for i in range(n):
        if day == pb[i][1]:
            k = pb[i+1:]
            for j in range(len(k)):
                if day == k[j][1]:
                    return False
    return True

def unique_month(month, pb):
    n = len(pb)
    for i in range(n):
        if month == pb[i][0]:
            k = pb[i+1:]
            for j in range(len(k)):
                if month == k[j][0]:
                    return False
    return True

def contains_unique_day(month, pb):
    new_pb = tuple(filter( lambda x: x[0] == month, pb))
    n = len(new_pb)
    for i in range(n):
        day = new_pb[i][1]
        if unique_day( day, pb):
            return True
    return False
