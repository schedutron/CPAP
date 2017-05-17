with open('redata.txt', 'r') as f:
    days = {}
    for eachLine in f:
        days[eachLine[:3]] = days.get(eachLine[:3], 0) + 1
    for day in days:
        print day, days[day]
