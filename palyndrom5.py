#check if the string is a polindrome

import re

def word_poly(s):
    pat = r'\ '
    s = re.sub(pat, '', s)
    l = len(s)

    for i in range(l//2):
        if s[i] != s[-1-i]:
            return False
    return True

print(word_poly('mr owl ate my metal worm'))