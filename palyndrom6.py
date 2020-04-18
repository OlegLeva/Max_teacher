def palindrom(s):
    i = 0
    j = len(s) - 1
    while i < j:
        # skip spaces
        if s[i] == ' ':
            i += 1
            continue
        if s[j] == ' ':
            j -= 1
            continue
        # check
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
print(palindrom('asdfdsa'))

'''if __name__ == '__main__':
    assert palindrom('mr owl ate my metal worm')
    assert palindrom('1')
    assert palindrom('121')
    assert palindrom('1  21')
    assert palindrom('1231') == False
    assert palindrom('  ')
'''