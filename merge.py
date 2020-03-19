
def merge(l1,l2):
    l = l1 + l2
    l = sorted(l)
    return l

print(merge([26,45,55],[47,49,99]))


def find(l, x):
    i = 0
    j = len(l)-1
    m = int(j/2)
    while l[m] != x and i < j:
        if x > l[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
    if i > j:
        return 'Нет такого'
    else:
        return m
print(find([26, 45, 47, 49, 55, 99], 47))