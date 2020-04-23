
def palindrom(s):

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == ' ':  i += 1
        while not s[i] and i < j:
            i += 1
        if s[j] == ' ':  j -= 1
        while not s[j] and i < j:
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
print(palindrom('mr owl ate my metal worm'))



