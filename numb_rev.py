def num_rev(x):
    y = 0
    if x > 0:
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
        print(y)
    elif x < 0:
        x *= -1
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
        print(-y)
num_rev(-87)