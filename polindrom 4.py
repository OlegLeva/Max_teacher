
#check if the string is a polindrome

def word_poly(word):
    s = word.replace(" ", "")
    l = len(s)

    for i in range(l//2):
        if s[i] != s[-1-i]:
            return False
    return True

print(word_poly('mr owl ate my metal worm'))


#check if the string is a polindrome

import re

def word_poly(word):
    pat = r'\,|\s|\:|\.|\-|\_'
    s = re.sub(pat, '')
    l = len(s)

    for i in range(l//2):
        if s[i] != s[-1-i]:
            return False
    return True

print(word_poly('mr owl ate my metal worm'))