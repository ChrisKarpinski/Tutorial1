# Exercise 2: 

name = input("What is your name? ")

yearOfBirth = input("In what year were you born in? ")

currentYear = input("What is the current year? ")

print ("Since it is " + currentYear + ", " + name + " must be between " + str(int(currentYear) - int(yearOfBirth)) + " or " + str(int(currentYear) - int(yearOfBirth) - 1) + " years old.")
