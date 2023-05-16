second = 1
minute = second * 60
hour = minute * 60
day = hour * 24
twentyEightMonth = 28 * day
thiryMonth = 30 * day
thirtyOneMonth = 31 * day
year = 365 * day
leapYear = 366 * day

print("Seconds Calculator!")
print("Find out how many seconds are in a set amount of time!")
print("What unit of time would you like to know the second count for?")
timeFrame = input(
    "Choose from: minute; hour; day; the month (jan-dec), year, or leap year- "
)
if timeFrame == "minute":
    print("there are", minute, "seconds in a minute!")
elif timeFrame == "hour":
    print("there are", hour, "seconds in a hour!")
elif timeFrame == "day":
    print("there are", day, "seconds in a day!")
elif timeFrame == "feb":
    print("there are", twentyEightMonth, "seconds in ", timeFrame, "!")
elif timeFrame == "jan" or timeFrame == "mar" or timeFrame == "may" or timeFrame == "jul" or timeFrame == "aug" or timeFrame == "oct" or timeFrame == "dec":
    print("there are", thirtyOneMonth, "seconds in ", timeFrame, "!")
elif timeFrame == "apr" or timeFrame == "jun" or timeFrame == "sep" or timeFrame == "nov":
    print("there are", thiryMonth, "seconds in ", timeFrame, "!")
elif timeFrame == "year":
    print("there are", year, "seconds in a year!")
elif timeFrame == "leap year":
    print("there are", leapYear, "seconds in a leap year!")
else:
  print("Sorry, that command wasn't recognized! Try again!")