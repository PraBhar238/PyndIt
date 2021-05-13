
# Writing a 'Guess the number' game in python

import random

print()
print()
print()

print('GGGGGGGG   UU    UU   EEEEEEE   SSSSSSS   SSSSSSS       IIIIIIII   TTTTTTTT')
print('GG         UU    UU   EE        SS        SS               II         TT   ')
print('GG  GGGG   UU    UU   EEEEEEE   SSSSSSS   SSSSSSS          II         TT   ')
print('GG    GG   UU    UU   EE             SS        SS          II         TT   ')
print('GGGGGGGG     UUUU     EEEEEEE   SSSSSSS   SSSSSSS       IIIIIIII      TT   ')

print()
print('Pick a range and guess the correct random number selected from it')
print()

print('Hey there what is your name ? ')
playername = input()
# This part is for getting the player name

print('Well ' + playername + ' pick a number for range from 1 to....')
playerselect = input()
# This part gets the range input from the player for picking the random number

print('Now between 1 and ' + str(playerselect) + ' i have selected a number try to guess the right answer, You have 5 chances')
# This part compiles both the name and range input from the player

theanswer = int(random.randint(1,int(playerselect)))
# This is the random number of the given range generator

for I in range(1,6):

    playeranswer = input()

    if theanswer == int(playeranswer):
        print('WOOOO correct you have won!!')
        break
    elif theanswer < int(playeranswer):
        print('You are way far off the answer, Try again you have ' + str(5 - int(I)) + ' chances')
    elif theanswer > int(playeranswer):
        print('You are too short from the answer, Try again you have ' + str(5 - int(I)) + ' chances')
    else:
        print('Error')
# This entire loop runs the answering with a countdown as chances

if I == 5:
    print()
    print('==-== * ==-==[ GAME OVER ]==-== * ==-== ')
    print('The answer i was thinking of was ' + str(theanswer))
# This part runs the gameover message and shows the answer if the player runs out of all the chances and does'nt get the answer

