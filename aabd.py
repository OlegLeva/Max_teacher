def num_rev(x):
    y = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return sign * y


print(num_rev(-87))