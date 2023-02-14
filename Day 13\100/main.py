#Grade Percentage Generator!
print("Welcome to Grade Percentage Generator!")
print("Enter values below to get your percentage.")
print()

#take user input and store as variables
test = input("Enter Test Name: ")
print("_____________________________________________")
total_score = int(input("Enter Total Test Score: "))
print("_____________________________________________")
score = int(input("Enter Your Test Score: "))
print("_____________________________________________")
print()

#calculate percentage
percentage = score / total_score * 100

#print percentage
if percentage >= 90:
    print("You got a perfect grade for", test, "🎉 Your percentage is", round(percentage, 2), "%", "That's an","\033[32m","A+" "\033[0m")
    print()

elif percentage >= 80 or percentage == 89:
    print("You got a great grade for", test, "👍 Your percentage is", round(percentage, 2), "%", "That's an","\033[32m","A" "\033[0m")
    print()

elif percentage >= 70 or percentage == 79:
    print("You got a good grade for", test, "🙂 Your percentage is", round(percentage, 2), "%", "That's a","\033[32m","B" "\033[0m")
    print()

elif percentage >= 60 or percentage == 69:
    print("You got an average grade for", test, "😕 Your percentage is", round(percentage, 2), "%", "That's a","\033[34m","C" "\033[0m")
    print()

elif percentage >= 50 or percentage == 59:
    print("You got a bad grade for", test, "😞 Your percentage is", round(percentage, 2), "%", "That's a","\033[33m","D" "\033[0m")
    print()
else:
    print("You got a poor grade for", test, "💔 Your percentage is", round(percentage, 2), "%", "That's an", "\033[31m","F" "\033[0m")