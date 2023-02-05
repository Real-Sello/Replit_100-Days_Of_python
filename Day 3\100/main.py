#The ultimate wacky recipe maker using strinng concatenation
#Ask for user input then store as variables
myName = input("Enter Name : ")
myFood = input("Meal for the day : ")
myPlant = input("Favorite edible plant to go with meal : ")
myMethod = input("Cooking method :  ")
myType = input("How would you describe a burnt plant? ")
myItem = input("Your choice of restaurantware? ")
myTime = input("What time would you like your meal to be ready? ")
print()
print("Tonight's MENU:")
#Print out a recipe page in concatenated format
print(myName,"'s order for the day is: ", myMethod, myFood, "with", myType, myPlant, "on a", myItem )