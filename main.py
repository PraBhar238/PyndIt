
import random

print()
print('     PPPPPPPP    YY      YY    NN      NN    DDDDDDDD         IIIIIIIIII    TTTTTTTTTT   ')
print('     PP    PP     YY    YY     NNN     NN    DD     DD            II            TT       ')
print('     PPPPPPPP       YYYY       NN NN   NN    DD     DD            II            TT       ')
print('     PP              YY        NN   NN NN    DD     DD            II            TT       ')
print('     PP              YY        NN     NNN    DDDDDDDD         IIIIIIIIII        TT       ')
print()
print('* Welcome to Pynd It, A game where you decide how the game plays by selecting a range of your desire.')
print('* The game then picks a random number from the range you selected ')
print('* The number of chances and the score also depend on the range you select and the way you play')
print('! Caution: Due to some ongoing developments advice to select 40 or above as range for best experience')
# The intro part of the game

print()
print('Please state your name')
playername = input()
# This part asks for the name of the user

print('Well ' + playername + ' pick a number for range from 0 to...... ')
playerselect = input()
# This part asks for range input from the user

chancemaker = int(playerselect) / 100 * 5
# This part creates chances based on your input range

print('Now, Between 0 and ' + str(playerselect) + ' a number has been chosen you have ' + (str(chancemaker)) + ' chances to guess it. Good luck')
# Putting together user data for profile building

theanswer = random.randint(0,int(playerselect))
print(theanswer)
# This is the code for choosing a random number from the users range

playeranswer = ''
I = ''
# defining a global variable to be used locally

for I in range(0, int(chancemaker)):
    playeranswer = input()

    if theanswer == int(playeranswer):
        print('!! CORRECT !!')
        break
    elif theanswer < int(playeranswer):
        print('You are way far off from the answer, Try again you have ' + str(int(chancemaker) - I - 1) + ' chances')
    elif theanswer > int(playeranswer):
        print('You are too short from the answer, Try again you have ' + str(int(chancemaker) - I - 1) + ' chances')
    else:
        print('Error')
# The loop that intakes input and runs chances for the user

if (int(chancemaker) - int(I)) != 0 and playeranswer != theanswer:
    print()
    print('Session ended')
    print('The answer i was thinking of was : ' + str(theanswer))
# Displays the result and end message of the game session after ending

print()
thescore = (int(chancemaker - I) / int(chancemaker) * 100)
print(' Your score: ~ ' + str(thescore))
print('---------------------')
print(' Out of:       100')
# This score system calculates scores based on chances user used

