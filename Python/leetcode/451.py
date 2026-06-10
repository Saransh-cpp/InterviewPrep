def frequencySort(s):
    d = [0] * 128
    for c in s:
        d[ord(c)] += 1

    return "".join(sorted(s, key = lambda x: (-d[ord(x)], x)))
