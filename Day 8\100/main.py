#Affirmations Generator
print("============================================")
print("🌞 Welcome to the Affirmations Generator 🌞!")
print("============================================")
print("Enter some information to generate a random affirmation :")
print()
#INPUT
#Ask user information and store variables
myName = input("Name: ")
today = input("Day: ")
myMood = input("Mood: ")
print()

#Set default variables
greetings = "Hello "+ myName + "!!"
closing = "Cheers " + myName + ", " + "have a great " + today + "!!!"

#MOOD
#Neutral
monday = "Read this aloud : I am worthy of success and abundance, and I am capable of achieving my goals."
tuesday = "Read this aloud : I am filled with positive energy and strength, and I choose to focus on the good in every situation."
wednesday = "Read this aloud : I am confident in my abilities and trust in the path that is unfolding for me."
thursday = "Read this aloud : I am grateful for all the blessings in my life, and I choose to see the beauty and joy in every moment."
friday = "Read this aloud : I am deserving of love and happiness, and I attract positivity and success into my life."
saturday = "Read this aloud : Today, I choose to focus on all the positive things in my life and let go of any negativity. I am grateful for my strengths and abilities, and I trust in my journey."
sunday = "Read this aloud : Today, I am at peace and full of joy. I let go of stress and embrace rest and renewal. I am worthy of love and happiness, and I am surrounded by abundance in all aspects of my life."

#Sad
sadMonday = "Take a deep breath, let go of the worries of the past, and embrace a new week full of opportunities and growth."
sadTuesday = "Remember, every small step forward is still progress. Keep going, you've got this!"
sadWednesday = "Think about all the things you are grateful for and allow those positive feelings to uplift your day."
sadThursday = "Take a moment to stretch, move your body, and get some fresh air. It's a small step to feeling revitalized."
sadFriday = "You've made it to the end of the week, give yourself a pat on the back and plan some fun activities to celebrate."
sadSaturday = "Today is a new opportunity to live life to the fullest and create memories to cherish forever. Embrace the moment and enjoy the journey."
sadSunday = "Take a deep breath and let go of any stress or worries. Today is a day to recharge, relax, and rejuvenate. Enjoy the peace and tranquility that surrounds you."

#Happy
happyMonday = "Start this Monday with a smile and a positive attitude. You got this! 💪"
happyTuesday = "Embrace the new opportunities and adventures that this Tuesday will bring. Have a great day! 🌞"
happyWednesday = "Halfway through the week, keep pushing forward and spreading joy. You're doing great! 😃"
happyThursday = "Take time to appreciate the little things today and let them bring a smile to your face. Happy Thursday! 🌻"
happyFriday = "It's finally Friday! Celebrate all your hard work and enjoy the weekend. Have a fantastic day! 🎉"
happySaturday = "Embrace the beauty of the present moment and enjoy all the simple pleasures that today has to offer. Happy Saturday!"
happySunday =  "Today is a day of rest and rejuvenation. I take care of my mind, body, and soul, and I am filled with peace and gratitude."

#IF & NESTED IF STATEMENTS, CONCATENATION and OUTPUT
#Output for Monday
if today == "Monday" or today == "monday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happyMonday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadMonday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + monday + " " + closing)
        print()

#Output for Tuesday
if today == "Tuesday" or today == "tuesday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happyTuesday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadTuesday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + tuesday + " " + closing)
        print()

#Output for Wednesday
elif today == "Wednesday" or today == "wednesday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happyWednesday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadWednesday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + wednesday + " " + closing)
        print()

#Output for Thursday
elif today == "Thursday" or today == "thursday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happyThursday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadThursday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + thursday + " " + closing)
        print()

#Output for Friday
elif today == "Friday" or today == "friday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happyFriday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadFriday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + friday + " " + closing)
        print()

#Output for Saturday
elif today == "Saturday" or today == "saturday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happySaturday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadSaturday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + saturday + " " + closing)
        print()

#Output for Sunday
elif today == "Sunday" or today == "sunday":
    if myMood == "Happy" or myMood == "happy":
        print(greetings + " " + happySunday + " " + closing)
        print()
    elif myMood == "Sad" or myMood == "sad":
        print(greetings + " " + sadSunday + " " + closing)
        print()
    elif myMood == "Neutral" or myMood == "neutral":
        print(greetings + " " + sunday + " " + closing)
        print()


#Catch Everything else
else:
    print("Enter some information to generate a random affirmation")
    print("=======================================================")
    print()
