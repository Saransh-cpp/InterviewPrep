def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return recurse(s, len(s))

def recurse(s, n):
    if n <= n // 2:
        return True
    if s[len(s) - n] != s[n - 1]:
        return False
    return recurse(s, n - 1)
