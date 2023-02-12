#Generation Generator
#Generate & print out generation according to user input
#Ask user input and typecast to int and store
print("=========================================")
print("💯🌟 Welcome to Generation Generator 🌟💯")
print("=========================================")
print()
print("===========================================================")
print("Input your year below to see what generation you're part of")
print("===========================================================")
print()
myYear = int(input("What year were you born? : "))
print()

#Check what year the input corresponds with, Using comparison statements
if myYear >= 1925 and myYear <= 1946:
    print("You are a traditionalist")
    print()
elif myYear >= 1947 and myYear <= 1964:
    print("You are a Baby Boomer")
    print()
elif myYear >= 1965 and myYear <= 1981:
    print("You are a Generation X")
    print()
elif myYear >= 1982 and myYear <= 1995:
    print("You are a Millenial")
    print()
elif myYear >= 1996 and myYear <= 2015:
    print("You are a Generation Z")
    print()
else:
    print("Must be a dinosaur or a robot, You are not a traditionalist or Baby Boomer or Generation X or Millenial or Generation Z")
    print()