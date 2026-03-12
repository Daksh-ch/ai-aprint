from datetime import date

current_year = date.today().year

birth = int(input("Enter your birth year: "))
age = current_year - birth

print("Your age is: " + str(age))