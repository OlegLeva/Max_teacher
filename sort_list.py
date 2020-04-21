
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

