Period, WorkingDay, PausePeriod = map(int, input().split())
S = input()
SReverse = S[::-1]

"""
Calculate the day that you can work the fastest and the day that you can work
the slowest. If two days coincide, that day is always a working day.
"""
earliest_days = [-1 for _ in range(Period)]
slowest_days = [-2 for _ in range(Period)]

for days in (earliest_days, slowest_days):
    i_day = 0
    if days == earliest_days:
        i_work_day = 1
        diff_from_next_work = 1
        passion_days = S
    else:
        i_work_day = WorkingDay
        diff_from_next_work = - 1
        passion_days = SReverse
    
    while 1 <= i_work_day and i_work_day <= WorkingDay:
        if passion_days[i_day] == 'o':
            days[i_day] = i_work_day
            i_work_day += diff_from_next_work
            i_day += PausePeriod
        i_day += 1

slowest_days.reverse()
for i_day in range(Period):
    if earliest_days[i_day] == slowest_days[i_day]:
        print(i_day + 1)

exit()