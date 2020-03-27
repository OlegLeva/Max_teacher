'''
did not work without translating to a string ((
'''

for n in range(100000, 1000000):
    n = str(n)
    if (n[0] + n[1] + n[2]) == (n[3] + n[4] +n[5]):
        print(n)
