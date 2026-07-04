def insert(intervals, newInterval):
    if not intervals: return [newInterval]

    res = []

    i = 0
    while i < len(intervals):
        if intervals[i][1] >= newInterval[0]:
            break
        res.append(intervals[i])
        i += 1
    
    if i == len(intervals): return intervals + [newInterval]
    overlap_start = intervals[i]

    i = len(intervals) - 1
    while i > -1:
        if intervals[i][0] <= newInterval[1]:
            break
        i -= 1

    if i == -1: return [newInterval] + intervals
    overlap_end = intervals[i]

    res.append(
        [
            min(overlap_start[0], newInterval[0]),
            max(overlap_end[1], newInterval[1])
        ]
    )
    res += intervals[i + 1:]

    return res
