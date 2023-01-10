# importing modules and packages
import emoji
import os



# defining function of actual game to call in “main.py”
def ticTacEmoji():



  # defining function to return to the main menu once game has finished
  def returnMainMenu():
    mainMenu = input('\n\nType M to return to the main menu!')
    mainMenu = mainMenu.upper()
    if mainMenu == 'M':
      return False
    else:
      print('Not a valid option. Please try again')
  
  

  # defining function of drawing the startup game board with numbers in the blanks 
  def drawGameBoard(numbers):
    # printing original gameboard, "numbers[0]" etc is called and replaced from "numbers" list later on in code with user's entry 
    print('\n')
    print('\t     |     |')
    print('\t ',numbers[0],' | ',numbers[1],' | ',numbers[2])
    print('\t_____+_____+_____')
    print('\t     |     |')
    print('\t ',numbers[3],' | ',numbers[4],' | ',numbers[5])
    print('\t_____+_____+_____')
    print('\t     |     |')
    print('\t ',numbers[6],' | ',numbers[7],' | ',numbers[8])
    print('\t     |     |')
    print('\n')
  

  
  # defining function of each player's icon, (headphones or videogame emoji) imported using the emoji package
  def getPlayerIcon():
    emojiOne = emoji.emojize(":headphone:")
    emojiTwo = emoji.emojize(":video_game:")
    print('\nThe first player will be playing as the following emoji: ', emojiOne, '.\nThe second player will be playing as the following emoji: ', emojiTwo, '.')
    return emojiOne, emojiTwo
  
  

  # defining the function that places the actual turn on the board using three arguments, "numbers" list, marker of player's emoji, and move of user's choice to place their emoji 
  def placeTurn(numbers, marker, move):

    # move is subtracted by 1 as index of "numbers" list starts at 0 instead of 1 to correlate with the defined numbers displayed on "drawGameBoard"
    numbers[move - 1] = marker
    return numbers
  

  
  # defining function to check if number to replace with emoji is empty or not using the arguments "numbers" and "move"
  def checkEmptySpace(numbers, move):

    # "numbers[move-1]" calls the emoji of the player from index of 0-8 by subtracting 1. "emoji.demojize" converts the actual emoji back into the string value, ("videogame"/"headphones") and assigns to variable "val" 
    val = emoji.demojize(numbers[move - 1])
    count = len(val)

    # in gameboard, numbers 1-9 are replaced by the player's emoji, if "count" (length of the number of characters) is equal to 1, then = empty space (since the original numbers 1-9 are all one character only). However, if original number 1-9 on gameboard is replaced by an emoji, then the emoji.demojize and len(val) results in a character length bigger than 1, so = space is not empty
    return count == 1
  

  
  # defining function to get user input of choice from 1-9 to replace on gameboard using argument "numbers"
  def getUserTurn(numbers):

    # exception handling if user does not enter a number from 1-9
    try:
      turn = input('Select and type an empty space between the numbers 1 to 9 on the board: ')

      # calling checkEmptySpace function as the integer of the user input above (int(turn))
      while checkEmptySpace(numbers,int(turn)) == False:
        turn = input('This space has already been taken. Please choose another number to mark.')
      return turn 
    except:

      # exception handling so that the function getUserTurn(numbers) is called again and returned if user does not enter appropriate input
      return getUserTurn(numbers)
    

  
  # defining function to check win by lining up all three emojis in a row using arguments "numbers" and "marker"
  def winCheck(numbers, marker):

      # if statements that equal to the marker (which is the players' emoji icon), and sequence of 3 numbers which should be replaced by same emoji
      if marker == numbers[0] == numbers[1] == numbers[2]:
          return True
      if marker == numbers[3] == numbers[4] == numbers[5]:
          return True
      if marker == numbers[6] == numbers[7] == numbers[8]:
          return True
      if marker == numbers[0] == numbers[3] == numbers[6]:
          return True
      if marker == numbers[1] == numbers[4] == numbers[7]:
          return True
      if marker == numbers[2] == numbers[5] == numbers[8]:
          return True
      if marker == numbers[0] == numbers[4] == numbers[8]:
          return True
      if marker == numbers[2] == numbers[4] == numbers[6]:
          return True
      return False
  
  

  # clearing previous menu display from console
  os.system('clear')
  print('Welcome to Tic-Tac-Emoji!\n\nThis is a two player game so grab a partner!')

  # assigning "players" variable to function "getPlayerIcon()" as a list
  players = getPlayerIcon() 

  # assigning the variable "numbers" as the numerical characters 1-9,
  numbers = '1,2,3,4,5,6,7,8,9'.split(',')
  print('Below you will find the numerical set up of the tic-tac-emoji gameboard')

  # for loop that executes for length of "numbers" (0-8 since indexing counts from 0, not 1)
  for i in range(len(numbers)):

    # calling the function of "drawGameBoard", with the argument replaced by the "numbers" variable 1-9 
    drawGameBoard(numbers)
    
    # assigning the variable "marker" as either headphones or videogames emoji, "i % 2" determines which player's turn as i starts off as 0 and modulus alternates between 0 (player 1) and 1 (player 2)
    marker = players[i % 2]
    print('It is', marker, '\'s turn.')
    
    # assigning the variable "move" to the called function getUserTurn with the argument "numbers" for the user's choice to place their emoji on the board from places 1 to 9
    move = getUserTurn(numbers)
    
    # calling "placeTurn" function with last argument of integer of "move" variable seen above
    placeTurn(numbers, marker,int(move))

    # if statement to check if move wins game by calling function "winCheck"
    if winCheck(numbers, marker):
      drawGameBoard(numbers)
      print('Congratulations!', marker, 'WON!', emoji.emojize(":trophy:"))
      if returnMainMenu() == False:
        break

    # elif statement if "i" = 8 as that means a full gameboard (remember, not 9 because the index counts from 0 not 1!)
    elif i == 8:
      drawGameBoard(numbers)
      print('There are no more spaces on the board. It\'s a tie...Game over', emoji.emojize(":crying_face:")) 
      if returnMainMenu() == False:
        break