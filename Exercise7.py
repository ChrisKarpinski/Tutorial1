# Exercise 7: 

month = input("What month? ")

validMonth = True

if month == "january":
    numberDays = 31
elif month == "february":
    year = int(input("What year is it? "))
    
    if year%4 == 0 and not(year%4 == 0 and year%100 == 0 and year%400 != 0):
        leapYear = True
    else: 
        leapYear = False
    
    if leapYear:
        numberDays = 29
    else:  
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
    if month == "february" and leapYear:
        print(month + " has " + str(numberDays) + " days in " + str(year))
    elif month == "february" and not(leapYear):
        print(month + " has " + str(numberDays) + " days in " + str(year))
    else:     
        print(month + " has " + str(numberDays) + " days.")
        
