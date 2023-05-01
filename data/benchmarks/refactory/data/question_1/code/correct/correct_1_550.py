def search (x, s):
    if not s:
        return 0
    for i in range (len(s)):
        if x<=s[i]:
            return i
    return i+1
