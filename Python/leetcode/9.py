def isPalindrome(x):
    if x < 0: return False

    orig = x
    n = 0

    while x != 0:
        n = n * 10 + x % 10
        x = x // 10
    
    return orig == n


if __name__ == "__main__":
    x = 121
    print(isPalindrome(121))

    x = -121
    print(isPalindrome(x))

    x = 10
    print(isPalindrome(x))
