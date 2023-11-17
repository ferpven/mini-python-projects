def add_time(start, duration, day=None):

    startTime = start.split(" ")
    #print("Start time is: " + (startTime[0].split(":")[0]))
    #print(startTime[1])

    week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    #print(week)

    finalTimeHour = (int(startTime[0].split(":")[0])) + int(duration.split(":")[0])
    finalTimeMin = (int(startTime[0].split(":")[1])) + int(duration.split(":")[1])
    finalAPM = startTime[1]
    manyDays = 0
    nextDay = 0

    if finalTimeMin >= 60:
        finalTimeMin = finalTimeMin % 60
        finalTimeHour += 1

    if finalTimeHour >= 12 and finalTimeMin > 0:
        times = int(finalTimeHour / 12)
        if finalTimeHour > 12:
            finalTimeHour = finalTimeHour % 12
        if finalTimeHour == 0:
            finalTimeHour += 12
        while times > 0:
            if finalAPM == "PM":
                finalAPM = "AM"
                nextDay += 1
            elif finalAPM == "AM":
                finalAPM = "PM"
            times -= 1
        
    if finalTimeMin < 10:
        finalTimeMin = "0" + str(finalTimeMin)

    new_time = ("{}:{} {}").format(finalTimeHour, finalTimeMin, finalAPM)

    if day != None:
        if nextDay == 0:
            new_time += (", {}").format(day)
        else:
            needindex = (week.index(day.lower()) + nextDay) % 7
            new_time += (", {}").format(week[needindex].capitalize())
            
    if int(duration.split(":")[0]) >= 24:
        manyDays += round((int(duration.split(":")[0]) / 24) + 1)

        if int(duration.split(":")[0]) < 12 or nextDay == 1:
            new_time += " (next day)"
        else:
            new_time += (" ({} days later)").format(int(manyDays))
    elif startTime[1] == "PM" and finalAPM == "AM":
        manyDays += 1
        if int(duration.split(":")[0]) < 12 or manyDays == 1:
            new_time += " (next day)"
 
    return new_time