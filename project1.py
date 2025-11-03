total_rain = 0.0
total_wind = 0.0
days = 0
sentinelValue = True
while sentinelValue:
    user_input = input("Enter the rain value followed by the wind value: -1.0 to end\n")
    if user_input.strip() == "-1.0":
        sentinelValue = False
    else:
        myList = user_input.split()
        if len(myList) < 2:
            print("Please enter 2 values")
        else:
            rain, wind = map(float, myList)
            if rain == -1.0:
                sentinelValue = False
            else:
                total_rain += rain
                total_wind += wind
                days += 1
if days > 0:
    avg_rain = total_rain / days
    avg_wind = total_wind / days
    severity_of_weather = (avg_rain * 10) + avg_wind
    print(f"The average rain is {avg_rain:.1f} inches\n")
    print(f"The average wind is {avg_wind:.1f} mph\n")
    print(f"The weather severity for these {days} readings is: {severity_of_weather:.1f}")
else:
    print("No data was entered.")



