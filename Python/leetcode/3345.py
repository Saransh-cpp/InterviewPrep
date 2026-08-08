def smallestNumber(n, t):
    while True:
        if not product(n) % t:
            return n
        n += 1

def product(n):
    p = 1
    while n:
        p *= n % 10
        n //= 10
    return p
