def combinationSum2(candidates, target):
    res = set()
    recurse(0, [], candidates, target, res)
    return [list(x) for x in res]

def recurse(ind, curr, candidates, target, res):
    if target <= 0 or ind >= len(candidates):
        if target == 0:
            curr.sort()
            res.add(tuple(curr))
        return
    recurse(ind + 1, curr + [candidates[ind]], candidates, target - candidates[ind], res)
    recurse(ind + 1, curr, candidates, target, res)


def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    recurse(0, [], candidates, target, res)
    return res

def recurse(self, ind, curr, candidates, target, res):
    if target == 0:
        res += [curr]
        return

    for i in range(ind, len(candidates)):
        if i > ind and candidates[i] == candidates[i - 1]: continue
        if candidates[i] > target: break
        recurse(i + 1, curr + [candidates[i]], candidates, target - candidates[i], res)


def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    recurse(0, [], candidates, target, res)
    return res

def recurse(self, ind, curr, candidates, target, res):
    if target <= 0 or ind >= len(candidates):
        if target == 0:
            res += [curr]
        return

    recurse(ind + 1, curr + [candidates[ind]], candidates, target - candidates[ind], res)

    for i in range(ind + 1, len(candidates)):
        if candidates[i] != candidates[i - 1]:
            recurse(i, curr, candidates, target, res)
            break
