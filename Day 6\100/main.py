#Simple login program that accepts username and password
#ask for username and password, store as variables
print("Welcome to the simple but Secure Login")
print()
user = input("Enter username: ")
lock = input("Enter Password: ")
print()

#Check if user exists and crededntials match
#user 1
if user == "thor" and lock == "stormbreaker":
  print(""" Welcome Odinson and Greetings from the mortal realm! I hope this message finds you in good health and spirits. Your bravery and strength continue to inspire us all, and I wanted to take a moment to express my admiration for your accomplishments.

Thank you for being a shining example of courage and determination. Your unwavering commitment to protecting the Nine Realms serves as a reminder that even in the darkest of times, hope prevails.

Stay safe and keep wielding Mjolnir with pride.
  """)
  print()

#user 2
elif user == "ironman" and lock == "mspepper":
  print("""Hello Mr Stark, I just wanted to take a moment to express my admiration for your strength, determination, and unwavering spirit. Your unwavering commitment to pushing your limits and pushing the boundaries of what is possible inspires so many of us. Thank you for being a true embodiment of the human spirit and for reminding us all of the limitless potential within each of us.
  """)
  print()

#user 3
elif user == "captain" and lock == "firstSoldier":
  print("""Salute Captain, Thank you for always standing up for what's right and being a true symbol of bravery and patriotism. Your unwavering commitment to justice is truly inspiring.
""")
  print()

#user 4
elif user == "strange" and lock == "abracadabra":
  print("""Dear Dr Steven Strange, Your mastery of the mystical arts is truly remarkable. Your ability to bend reality and protect the world from interdimensional threats is greatly appreciated.
""")
  print()

#user 5
elif user == "hulk" and lock == "smash":
  print("""Bruce aka The Hulk, Your raw strength and power are unmatched. Despite your anger, you always manage to control your rage and use it for the greater good. Thank you for being a defender of the innocent.
""")
  print()

#catch everything else
else:
  print("No match. Please enter matching credentials")
  print()