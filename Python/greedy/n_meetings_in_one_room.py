def maxMeetings(start, end):
    pairs = [(x, y) for x, y in zip(start, end)]
    pairs.sort(key=lambda x: x[1])
    meetings = 1
    last_time = pairs[0][1]
    i = 1
    while i < len(pairs):
        if pairs[i][0] > last_time:
            meetings += 1
            last_time = pairs[i][1]
            i += 1
        else:
            while i < len(pairs) and pairs[i][0] <= last_time:
                i += 1
    return meetings
