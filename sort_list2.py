
def merge(l1):
    res = []
    res.append(l1[0])
    i = 0
    while i < len(l1)-1:
        if l1[i] < l1[i+1]:
            res.append(l1[i+1])
        if l1[i] == l1[i+1]:
            pass
        i += 1
    return res

print(merge([-1,-1, 0, 1, 2, 2, 3, 3, 5, 7, 8, 9]))