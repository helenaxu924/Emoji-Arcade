# Helena Xu
# July 23rd, 2021
# Xu_[EMOJIARCADE].py
# an arcade that consists of three separate emoji-themed games, 1 multiplyer and the rest singular, each game is based in its own file and called to “main.py” using functions and imports  



# loop control
flag = True 

# importing modules and packages 
import os
from art import text2art
from guess_the_emoji import guessTheEmoji
from tic_tac_emoji import ticTacEmoji
from emoji_says import emojiSays

import time



# defining function to display intro screen
def displayIntroScreen():
  print('Welcome to the Emoji Arcade!\n\nYou can choose between three emoji-related games below to play from.')
  print('You also have the options of help, and quitting the program.') 

# defining function to display menu options
def showMenu():
  print('\n       MENU')
  print('=====================')
  print('G for Guess The Emoji')
  print('T for Tic-Tac-Emoji')
  print('E for Emoji-Says')
  print('H for help')
  print('Q to quit')
  print('===================== \n')

# defining function to get user option
def getChoice():
  choice = input('Enter a letter to select your option: ')
  return choice

# defining function to display help text
def showHelp():
  print('This program is an emoji-themed arcade with three different games that players can choose from. The instructions for each game will be presented when you enter the game. Once you finish the game you can return to the menu and play another game or replay the same game. Good luck!')
  print('You can quit this program from the main menu by pressing Q')
  time.sleep(15)

# while loop for user input and calling to appropriate function based on input
while flag == True:

  # clear console for previous display when user finishes a game and re-enters the main menu
  os.system('clear') 

  # using text2art from imported art package to print ASCII text using chosen font
  # the "\a" sets off a terminal bell for a short sound effect!
  print('\a')
  print(text2art('THE', font='slant'))
  time.sleep(1)
  print('\a')
  print(text2art('EMOJI', font='slant'))
  time.sleep(1)
  print('\a')
  print(text2art('ARCADE', font='slant'))
  displayIntroScreen()
  showMenu()
  userChoice=getChoice()
  if userChoice == 'H':
    showHelp()
  elif userChoice == 'Q':
    flag = False
  elif userChoice == 'G':
    guessTheEmoji()
  elif userChoice == 'T':
    ticTacEmoji()
  elif userChoice == 'E':
    emojiSays()
  else:
    # if user does not enter a valid letter to begin
    print('Not a valid choice. Only G, T, E, Q, and H are valid choices')
print('Program Ending.')
 