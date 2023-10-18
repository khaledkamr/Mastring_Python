
def add_time(start_time, duration_time, starting_day = "unknown"):

    S_hour = start_time[0 : start_time.find(':')]
    if(start_time.find('PM') != -1):
        S_minute = start_time[start_time.find(':') + 1 : start_time.find('PM')]

    else:
        S_minute = start_time[start_time.find(':') + 1 : start_time.find('AM')]
    D_hour = duration_time[0 : duration_time.find(':')]
    D_minute = duration_time[duration_time.find(':') + 1 : ]

    hours = abs(int(S_hour) + int(D_hour))
    if(hours > 12):
        hours -= 12
    minutes = abs(int(S_minute) + int(D_minute))
    if(minutes > 59):
        pass

    print(f"{hours}:{minutes}")



start_time = input("Enter the starting time : ")
duration_time = input("Enter the duration time : ")
yesOrNo = input("would you like to add a starting day? (yes or no)")
if(yesOrNo == "yes"):
    starting_day = input("Enter the startig day : ")
    add_time(start_time, duration_time, starting_day)
else:
    add_time(start_time, duration_time)