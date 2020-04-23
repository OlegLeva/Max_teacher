
def merge(l1,l2):
    l = l1 + l2
    n = len(l)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            j += 1
        i += 1
    return l


print(merge( [1,2,2,3,3,7,9], [-1,0,5,8]))
