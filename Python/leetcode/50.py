def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    if (n % 2 == 1):
        return x * pow(x * x, (n - 1) / 2)
    else:
        return pow(x * x, n / 2)

def myPow(x, n):
    if n < 0:
        return 1 / pow(x, -n)
    return pow(x, n)


def myPow(x, n):
    invert = n < 0
    n = abs(n)
    ans = 1
    while n > 0:
        if (n % 2 == 1):
            ans *= x
            n = n - 1
        x *= x
        n = n / 2

    return 1 / ans if invert else ans
