def merge(l1, l2):

    res = []
    res1 = []

    i, j, r = 0, 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    # copy rest
    if i < len(l1):
        res.extend(l1[i:])
    if j < len(l2):
        res.extend(l2[j:])


    while r < len(res) - 1:
        if res[r] == res[r + 1]:
            del res[r]
        r += 1
    return res


print(merge([1, 2, 2, 3, 3, 3, 7, 9], [-1, -1, 0, 5, 5, 8]))
