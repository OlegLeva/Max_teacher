
def del_dubl(list3):

    j = len(list3)
    i = 0
    while i < j - 1:
        if list3[i] == list3[i+1]:
            del list3[i]
    i += 1


    return list3




print(del_dubl([-1, 0, 1, 2, 2, 3, 3, 5, 7, 8, 9]))