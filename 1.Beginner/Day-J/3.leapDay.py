# Refactoring the exercise Leap Day with Function.


def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 4:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysMonth(year, month)

print(days)