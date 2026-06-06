def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = []
    i = 0
    while i < len(intervals):
        j = i
        start = intervals[i][0]
        end = intervals[i][1]
        while j < len(intervals) - 1 and end >= intervals[j + 1][0]:
            end = max(intervals[j + 1][1], end)
            j += 1
        res.append([start, end])
        if i != j:
            i = j + 1
        else:
            i += 1
    return res


def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    res = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(intervals[i][1], end)
        else:
            res.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
    res.append([start, end])

    return res
