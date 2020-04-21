
def sor_lis (list1, list2):
    list3 = list1 + list2
    j = len(list3)
    n = 0
    while n < j - 1:
        i = 0
        while i < j - 1 - n:
            if list3[i] > list3[i+1]:
                list3[i], list3[i + 1] = list3[i + 1], list3[i]
            i += 1
        n += 1
    return list3
print(sor_lis([1,2,2,3,3,7,9], [-1,0,5,8]))

def merge(l1, l2):
    """
    >>> merge([1,2,3,4,6], [5,6,7,8])
    [1, 2, 3, 4, 5, 6, 6, 7, 8]
    >>> merge([1,2,3,4,5,6], [])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [1,2,3,4,5,6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([1],[2,3,4,5,6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([2,3,4,5,6],[1])
    [1, 2, 3, 4, 5, 6]
    """
    res = []
    i, j = 0, 0
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
    return res
