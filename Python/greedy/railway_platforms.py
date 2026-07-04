def findPlatform(Arrival, Departure):
    Arrival.sort()
    Departure.sort()
    Arrival = [int(a) for a in Arrival]
    Departure = [int(b) for b in Departure]
    arrival = 0
    departure = 0
    cnt = 0
    max_cnt = 0
    while arrival < len(Arrival) and departure < len(Departure):
        if Arrival[arrival] <= Departure[departure]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
            arrival += 1
        else:
            cnt -= 1
            departure += 1
    return max_cnt
