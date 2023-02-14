#Name the lyrics game
#A game that lets user guess the lyrics of a song then prints the number of times it took the user to guess the lyrics.
print("Welcome to the Lyrics Game!")
print()
print("Let's see if you can guess the lyrics of this song by Queen!")
print()
userName = input("Enter your name before you continue: ")
print("""
Mamaaa,
Just ______ a man,
Put a gun against his head, pulled my trigger,
Now he's dead
Mamaaa, life had just begun,
But now I've gone and thrown it all away
Mama, oooh,
Didn't mean to make you cry,
If I'm not back again this time tomorrow,
Carry on, carry on as if nothing really matters
Too late, my time has come,
Sends shivers down my spine, body's aching all
The time
Goodbye, everybody, I've got to go,
Gotta leave you all behind and face the truth
Mama, oooh
I don't want to die,
I sometimes wish I'd never been born at all.
""")
#Set a boolean while loop to true so the code loops
tries = 0
while True:
    tries += 1
    userLyrics = input("What are the missing lyrics ? ")
    if userLyrics == "killed":
        break
    else:
        #tries += 1
        print("That's not the correct lyrics, try again!")
        print()
if tries == 1:
    print("Marvellous!", userName, "You guessed the lyrics correctly!, It only took you", tries, "try.")
    print()

elif tries > 1 and tries <= 3:
    print("Great job!", userName, "You guessed the lyrics correctly!, It only took you", tries, "tries.")
    print()

elif tries > 3 and tries <= 6:
    print("Good job!", userName, "You guessed the lyrics correctly!, It took you", tries, "tries.")
    print()

else:
    print("Ok", userName, "Eventually you got it, It took you a whole", tries, "tries.")
print("End of the game!")