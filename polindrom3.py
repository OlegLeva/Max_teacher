
#Tortured to fight, does not go through "while"

def word_poly(word):
    x = len(word.replace(" ", ""))
    i = 0
    x -= 1
    while x - 1 >= i:
        if word[x - 1] == word[i]:
            i += 1
            return True
        else:
            return False

print(word_poly('abcbcba'))

# does not work(( I’m probably stupid((