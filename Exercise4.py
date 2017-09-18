# Exercise 4

days = input("How many days? ")

years = int(days)//365

months = (int(days) - 365*years)//30

weeks = (int(days) - 365*years - 30*months)//7

remainingDays = int(days) - 365*years - 30*months - 7*weeks

print(days + " is " + str(years) + " year(s), " + str(months) + " month(s), " + str(weeks) + " week(s), " + str(remainingDays) + " day(s).")
