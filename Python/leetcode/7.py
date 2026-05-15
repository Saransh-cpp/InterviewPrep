def reverse(x):
    new = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while(x != 0):
        new = new * 10 + x % 10
        x = x // 10

    return new * sign if new < 2 ** 31 - 1 else 0
