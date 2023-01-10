# importing modules and packages
import emoji
import random
import os
import time



# defining function of actual game to call in “main.py”
def guessTheEmoji():
  

  # defining function to return to the main menu once game has finished
  def returnMainMenu():
    mainMenu = input('\n\nType M to return to the main menu!')
    mainMenu = mainMenu.upper()
    if mainMenu == 'M':
      return False
    else:
      print('Not a valid option. Please try again')
  
  

  # dictionary assigning each emoji-combination key to the accompanied string value
  dict = {
    emoji.emojize(':artist_palette:') +  emoji.emojize(':ring:'):'colouring', 
    emoji.emojize(':sun_with_face:') + emoji.emojize (':glasses:'):'sunglasses', 
    emoji.emojize(':ear_of_corn:') + emoji.emojize (':dog_face:'):'corndog', 
    emoji.emojize(':cat_face:') + emoji.emojize(':fish:'):'catfish',
    emoji.emojize(':fire:') + emoji.emojize(':bathtub:'): 'hottub',
    emoji.emojize(':teacup_without_handle:') + emoji.emojize(':birthday_cake:'): 'cupcake', 
    emoji.emojize(':spider:') + emoji.emojize(':man:'): 'spiderman', 
    emoji.emojize(':books:') + emoji.emojize(':worm:'): 'bookworm', 
    emoji.emojize(':bird:') + emoji.emojize(':watch:'): 'birdwatch',
    emoji.emojize(':cheese_wedge:') + emoji.emojize(':hamburger:'):'cheeseburger'
  }
  
  

  # clearing previous menu display from console
  os.system('clear')

  # assigning variables and blank dictionary "newDict" for rearranged dictionary after each round
  incorrect = 0
  correct = 0
  newDict = {}

  # converting the keys of original dictionary into a list under the variable "keys"
  keys = list(dict.keys())

  # random shuffling the order of keys (emojis) in list 
  random.shuffle(keys)

  # for loop that adds and assigns the newly shuffled order of keys into "newDict"
  for key in keys:
    newDict[key] = dict[key]
  
  # printing game instructions
  print('Welcome to Guess The Emoji!')
  print('\n\nYou are presented with a combination of two emojis that have an equivalent meaning in English.')
  time.sleep(2)
  print('\n\nYou have 1 attempt to guess the word/phrase correctly for each emoji combination.')
  time.sleep(2)
  print('\n\nThe first amount of incorrect or correct guesses to reach 3 will determine if you lose or win.')
  ready = input('\n\nType S to begin!')
  ready = ready.upper()
  
  

  # while loop to check user input start and else statement at bottom prompting correct input
  while ready == 'S':

    # while loop that checks the condition of variables in each round, and loops unless the winning/losing condition has been met and prints appropriate result in else statement
    while incorrect < 3 and correct  < 3:

      # "[correct + incorrect]" adds total amount of rounds played and slices the "keys" list with the assigned emoji combination for that number and assigns to the variable "nextWord"
      nextWord = keys[correct + incorrect]

      # as "nextWord" variable = emoji combination from each round, "newDict" finds the assigned value (word) in the new, shuffled dictionary and assigns it to the variable "meaning"
      meaning = newDict[nextWord]

      # displaying for extra two seconds because when loop reruns the "os.system('clear')" immediately clears console 
      time.sleep(2)

      # clearing console of game instructions abd previous loop
      os.system('clear')
      print('Hint: all words/phrases do NOT contain spaces!\n')

      # displaying the emoji combination for user to guess and assigns to variable "guess" using lowercase method
      guess = input('Please guess the meaning of the following emojis:' + nextWord)
      guess = guess.lower()

      # if and else statements for checking user input, also adds 1 to incorrect/correct score based on result
      if guess == meaning:
        print('Yay! You got it!')
        correct += 1
      else:
        print('No, that\'s not it...Try the next one:')
        incorrect += 1

    # else statement for while loop when incorrect/correct score is more than 3 and accompanying condition of win or lose
    else:
      if incorrect >= 3:
        print('You have reached the end of your attempts. You lose',emoji.emojize(":crying_face:"))
        if returnMainMenu() == False:
          break
      else: 
        print('Congratulations! You have 3 correct guesses, you win!',emoji.emojize(":trophy:"))
        if returnMainMenu() == False:
          break
  else: 
    # if user does not enter "S" to begin
    print('\nEnter a valid input')
