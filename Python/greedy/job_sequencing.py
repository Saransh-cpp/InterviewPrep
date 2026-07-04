def JobScheduling(Jobs):
    Jobs.sort(key=lambda x: -x[2])
    max_days = max([x[1] for x in Jobs])
    n = [-1] * max_days
    profit = 0
    jobs = 0
    for job in Jobs:
        potential_position = job[1] - 1
        while potential_position >= 0 and n[potential_position] != -1:
            potential_position -= 1
        if potential_position >= 0:
            n[potential_position] = job[0]
            jobs += 1
            profit += job[2]
    return (jobs, profit)
