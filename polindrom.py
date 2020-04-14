#check if the string is a polindrome

def word_poli(x):
    if x == x[::-1]:
        return True
    elif x != x[::-1]:
        return False


print(word_poli('abcdcba'))

