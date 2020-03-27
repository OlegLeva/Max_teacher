'''does not work "int" problem'''

def tik():
    for num in range(100000, 1000000):
        num = int(num)
        if sum(num[:3]) == sum(num[-3:]):
             return num

tik()