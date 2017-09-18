#Exercise 6: 

month = input("What month? ")

validMonth = True

if month == "january":
    numberDays = 31
elif month == "february":
    isLeapYear = input("Is it a leap year? (Enter y or n) ")
    
    if isLeapYear == "y":
        numberDays = 29
    elif isLeapYear == "n":     
        numberDays = 28
elif month == "march":
    numberDays = 31
elif month == "april":
    numberDays = 30
elif month == "may":
    numberDays = 31
elif month == "june":
    numberDays = 30
elif month == "july":
    numberDays = 31
elif month == "august":
    numberDays = 31
elif month == "september":
    numberDays = 30
elif month == "october":
    numberDays = 31
elif month == "november":
    numberDays = 30
elif month == "december":
    numberDays = 31
else: 
    print("Invalid month")
    validMonth = False
    
if validMonth:
    if month == "february" and isLeapYear == "y":
        print(month + " has " + str(numberDays) + " in a leap year.")
    elif month == "february" and isLeapYear == "n":
        print(month + " has " + str(numberDays) + " in a non-leap year.")
    else:     
        print(month + " has " + str(numberDays) + " days.")
