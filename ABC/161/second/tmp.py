for earliest_day, slowest_day in zip(earliest_days, slowest_days):
    if earliest_day == slowest_day:
        print(earliest_days.index(earliest_day) + 1)