#calculate how many seconds in a year
print("Welcome to the seconds calculator!")
print()
print("Enter number of days this year has to calculate ceconds")
days = int(input("Enter number of days this year has: "))

year_days = 365
leap_days = 366
hours = 24
minutes = 60
seconds = 60

sec_year = year_days * hours * minutes * seconds
sec_leap = leap_days * hours * minutes * seconds

if days == 365:
    print("Number of ceconds in a 365 day year = ", sec_year)
elif days == 366:
  print("Number of seconds in a Leap year = ", sec_leap)