def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    i = 1
    intervals_kept = 1
    last_end = intervals[0][1]
    for i in range(len(intervals)):
        if intervals[i][0] >= last_end:
            last_end = intervals[i][1]
            intervals_kept += 1
    return len(intervals) - intervals_kept
