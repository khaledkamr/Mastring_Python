
def add_time(start_time, duration_time, starting_day = "unknown"):

    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    if (start_time.find('PM') != -1):
        S_time = 'PM'
    else:
        S_time = 'AM'

    S_hour = start_time[0 : start_time.find(':')]

    if(S_time == 'PM'):
        S_minute = start_time[start_time.find(':') + 1 : start_time.find('PM')].strip()
    else:
        S_minute = start_time[start_time.find(':') + 1 : start_time.find('AM')].strip()

    D_hour = duration_time[0 : duration_time.find(':')]
    D_minute = duration_time[duration_time.find(':') + 1 : ].strip()
    

    hours = int(S_hour) + int(D_hour)
    count = 0
    
    while(hours > 12):
        hours -= 12
        count += 1

        if (S_time == 'PM'):
            S_time = 'AM'

            if(starting_day != "unknown"):
                d = days.index(starting_day)
                starting_day = days[d + 1]
        else:
           S_time = "PM"
        
    minutes = int(S_minute) + int(D_minute)

    while(minutes > 59):
        minutes -= 60
        hours += 1
        count += 1

        if(hours > 12):
            hours -= 12
            if (S_time == 'PM'):
                S_time = 'AM'

                if(starting_day != "unknown"):
                    d = days.index(starting_day)
                    starting_day = days[d + 1]
            else:
                S_time = "PM"

    print(f"{hours}:{minutes} {S_time} ", end = "")

    if(starting_day == "unknown"):

        if(count == 1):
            print("(next day)")
        elif(count > 1):
            print(f"({count} days later)")
    else:
        print(f", {starting_day} ", end = "")

        if(count == 1):
            print("(next day)")
        elif(count > 1):
            print(f"({count} days later)")



start_time = input("Enter the starting time : ")
duration_time = input("Enter the duration time : ")
yesOrNo = input("would you like to add a starting day? (yes or no)")

if(yesOrNo == "yes"):
    starting_day = input("Enter the startig day : ")
    add_time(start_time, duration_time, starting_day)
else:
    add_time(start_time, duration_time)