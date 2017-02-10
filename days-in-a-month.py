months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "Movember": 30,
    "December": 31}

def normalize(month):
    return month[:1].upper() + month[1:].lower()

def isLeapYear(year):
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    return isLeapYear

while True:
    month = normalize(raw_input("What month do you want to know about? "))
    if len(month) == 0:
        print("Good bye")
        break
    if not month in months:
        print("%s in not a valid month" % month)
    else:
        days = months[month]
        if month == "February":
            year = int(input("What year is it? "))
            if isLeapYear(year):
                days = 29
        print("%s has %d days" % (month, days))
