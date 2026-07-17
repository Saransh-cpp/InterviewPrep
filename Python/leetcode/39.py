def combinationSum(candidates, target):
    res = []
    recurse(0, [], res, candidates, target)
    return res

def recurse(ind, curr, res, candidates, target):
    if target <= 0 or ind >= len(candidates):
        if target == 0:
            res += [curr]
        return
    recurse(ind, curr + [candidates[ind]], res, candidates, target - candidates[ind])
    recurse(ind + 1, curr, res, candidates, target)
