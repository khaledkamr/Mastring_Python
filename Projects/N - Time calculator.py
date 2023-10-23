
def add_time(start_time, duration_time, start_day = None):

    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    start_time, period = start_time.split()

    S_hour, S_minute = map(int, start_time.split(':'))
    S_hour %= 12

    D_hour, D_minute = map(int, duration_time.split(':'))
   
    hours = S_hour + D_hour
    minutes = S_minute + D_minute
    count = 0
    
    while(hours > 12):
        hours -= 12

        if (period == 'PM'):
            period = 'AM'
            count += 1

            if(start_day):
                d = days.index(start_day)
                start_day = days[d + 1]
        else:
           period = "PM"

    while(minutes > 59):
        minutes -= 60
        hours += 1

        if(hours > 12):
            hours -= 12
            if (period == 'PM'):
                period = 'AM'
                count += 1

                if(start_day):
                    d = days.index(start_day)
                    start_day = days[d + 1]
            else:
                period = "PM"     
        elif(hours == 12):
            if (period == 'PM'):
                period = 'AM'
                count += 1

                if(start_day):
                    d = days.index(start_day)
                    start_day = days[d + 1]
            else:
                period = "PM"   
    
    minutes = str(minutes)
    print(f"{hours}:{minutes.zfill(2)} {period}", end = "")

    if(start_day):
        if(count == 1):
            print("(next day)")
        elif(count > 1):
            print(f"({count} days later)")
    else:
        print(f", {start_day} ", end = "")

        if(count == 1):
            print("(next day)")
        elif(count > 1):
            print(f"({count} days later)")

start_time = input("Enter the starting time : ")
duration_time = input("Enter the duration time : ")
yesOrNo = input("would you like to add a starting day? (yes or no)").lower()

if(yesOrNo == "yes"):
    start_day = input("Enter the startig day : ").lower().capitalize()
    add_time(start_time, duration_time, start_day)
else:
    add_time(start_time, duration_time)