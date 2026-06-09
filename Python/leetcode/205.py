def isIsomorphic(s, t):
    d = {}
    for s_, t_ in zip(s, t):
        if s_ in d:
            if d[s_] != t_:
                return False
        elif t_ in d.values():
            return False
        d[s_] = t_

    return True
