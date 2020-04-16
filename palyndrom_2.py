
#check if the string is a polindrome

def word_poli(s):

    x = s.replace(" ", "")

    if x == x[::-1]:
        return True
    elif x != x[::-1]:
        return False


print(word_poli('mr owl ate my metal worm'))