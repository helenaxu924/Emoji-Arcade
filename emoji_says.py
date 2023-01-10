# importing modules and packages
import random
import emoji
import time
import os



# defining function of actual game to call in “main.py”
def emojiSays():
  

  
  # defining function to return to the main menu once game has finished
  def returnMainMenu():
    mainMenu = input('\n\nType M to return to the main menu!')
    mainMenu = mainMenu.upper()
    if mainMenu == 'M':
      return False
    else:
      print('Not a valid option. Please try again')
  
  

  # dictionary with keys as emojis using import emoji and each value as an assigned number from 1 to 4
  dict = {
    emoji.emojize(":house:") : '1',
    emoji.emojize (':wrapped_gift:') : '2',
    emoji.emojize(':pizza:') : '3', 
    emoji.emojize(':lion:') : '4'
    }
  

  
  # clear previous menu display from console
  os.system('clear')

  # converting dictionary keys into a list under the variable "keysList"
  keysList = list(dict.keys()) 

  # printing instructions for user with time.sleep between each
  print('Welcome to Emoji-Says!')
  print('\n\nThe rules are simple. A series of emojis will appear. You have a few seconds to memorize them before they dissapear. Your job is to type down the correct sequence of the shown emojis!')
  time.sleep(3)
  print('\n\nThe levels will get harder after each one, and you will win when you complete all 3 levels with no mistakes. \n\n')
  time.sleep(3)
  print('There will be an emoji-bank on the screen that you can refer to in order to assign each emoji to a number. Please make sure to take a look at it and familiarize yourself before you begin')
  print('\nEMOJI-BANK:', dict)
  time.sleep(2)
  print('\n\nBeginning level one...')

  # input from user indicating ready to start
  ready = input('\n\nType S to begin!')
  ready = ready.upper()

  # assigning the variable "level" as 1 (user begins on level 1)
  level = 1

  while ready == 'S':
    # clearing console of instructions
    os.system('clear')

    # assigning the variables "question" and "answer" as a blank list
    question = [] 
    answer = [] 

    # for loop that loops through "key" in the list of "keysList" from dictionary as assigned at the top 
    for key in keysList:

      # nested for loop with range from 0 to current level (remember level variable starts at 1) 
      for num in range(0, level):

        # shuffles the keysList of emojis using import random so the order of keys is different
        random.shuffle(keysList)

        # appending the blank "question" list with the emojis for each level. Each level increments by 4 more emojis since it loops twice when level is 2, three times when level is 3, etc 
        question.append(key)

        # appending the blank "answer" list with the values of the keys (emojis) for each level (which is called by using dict[key])
        answer.append(dict[key])



    # assigning the variable "valueList" as a blank list
    valueList = []

    # for loop that runs through the range of 0 to  length of the "question" list
    for q in range(0, len(question)):

      # printing emojibank dictionary to display after each clear.console at bottom of loop
      print('EMOJI-BANK:', dict)

      # appending the blank "valueList" list with each of the emojis from the "question" list based on how many times the for loop has ran for (q)
      valueList.append(question[q])

      # prints the emojis to be memorized as well as the '\a' sets off a terminal bell for a short sound effect!
      print('\a\nMEMORIZE...\n\n',valueList)

      # nested if else statement to check if q is the last emoji in "question" list (len(question) subtracts 1 due to index beginning at 0 instead of 1)
      if q == (len(question) - 1):

        # last loop gets 3 extra seconds to display as all of the emojis for the level has finished printing
        time.sleep(4)
      else:

        # for all other loops add 1 extra second to display
        time.sleep(1)

      # clearing the console to avoid duplication of emojis and so user can't see the emojis still on console history
      os.system('clear')
    

    
    # since console is cleared, reprinting emojibank for the user to refer to when they guess under variable "guess" input
    print('EMOJI-BANK:', dict)
    guess = input('\nType the emojis that were shown using the same format as displayed in the EMOJI-BANK. Please separate each with a comma: ')

    # user guess converted to list under "guess" variable
    guess = guess.split(',')
    
    

    # if and else statements for checking answer
    if guess == answer:
      level += 1

      # since level variable starts at 1, user wins when level = 4
      if level == 4:
        print('\nHooray, you did it! Awesome memorizing... you win!',emoji.emojize(":trophy:"))

        # calls function to return to main menu
        if returnMainMenu() == False:
          break

      # printing of congrats and new level will only happen if level is not 4 yet
      print('\nCongratulations! You got it... you are advancing to level:', level)

      # time.sleep(4) stops the console from clearing immediately when loop runs again
      time.sleep(4)
    else:
      print('\nOh no! You did not memorize the sequence of emojis correctly. You lose...game over', emoji.emojize(":crying_face:"))
      if returnMainMenu() == False:
        break
  else:
    # if user does not enter "S" to begin
    print('\nEnter a valid input')