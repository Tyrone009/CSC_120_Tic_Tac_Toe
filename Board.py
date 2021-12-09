#creating an array that contains an array, which is an two dimensional array.
myBoard = [
    ["-", "-", "-"], #this is the first index containing an array with a length of three elements
    ["-", "-", "-"], #this is the second index containing an array with a length of three elements
    ["-", "-", "-"] #this is the third index containing an array with a length of three elements
]
player = True
numberof_turns = 0
def print_myBoard(myBoard): #creating a print myBoard function to print myBoard
    for row in myBoard: #creating for loop for row in myBoard
        for slot in row: #nested for loop for slot in row of myBoard
            print(f"{slot} ", end="") #recognized slot as a predefined variable by using an f string
        print() #prints out a row after a new line

print_myBoard(myBoard) #prints out myBoard

def quit(user_TicTacToe): #creating a quit function
  if user_TicTacToe == "'q": #Gives the user the option to quit
      print("Thanks for playing") #Prints a message on the screen to the user which says thanks for playing.
      return True #Allows the user to quit playing the game.
  else: return False #This means the user wants to keep playing the game.

def check_mark(user_TicTacToe): #check mark function to check if a mark can be placed on the board
#checks to see if it is a letter
   if not isalpha(user_TicTacToe): return False
    #checks to see if the letter is an X or 0
   return True


def user_TicTacToe(args):
    pass


def bounds():
 if not boundaries(user_TicTacToe): #If statement that determines whether the input of the user are within the boundaries or are valid entries.
    return "False" #The letter entered by the user is not valid or within the boundaries of the game.

    return "True" #The letter entered by the user is valid and are within the boundaries of the game.


def isalpha(user_TicTacToe):
    if not user_TicTacToe.isalpha(): #if user input is not a letter
        print("The user entry is not valid.") #Prints the user entry is not valid
        return False #The entry of the user was not a letter
    else: return True #The entry of the user was a letter

def boundaries(user_TicTacToe2):
    if user_TicTacToe2 is not input("X") or user_TicTacToe2 is not input("O"): #if statement to determine whether the letter entered by the user is an X or O
        print("The letter entered is forbidden.") #tells the user the letter that entered is forbidden
        return False
    else: return True #States that the letter entered by the user are within the boundaries

def istaken(coords, myBoard):
    row = coords[0]
    col = coords[1]
    if myBoard[row][col] != "-": #If statement to determine if the place on the board is taken.
        print("This place is taken.") #Prints the place is taken so user cannot place a mark at that place on the board.
        return True
    else: return False #This means the place on the board is not taken, which returns a false Boolean value.




def coordinates(user_TicTacToe):
    row = user_TicTacToe / 3
    col = user_TicTacToe
    if col > 2 : col = int(col % 3)
    return (row, col)

def add_to_myBoard(coords, myBoard, live_user):

 def present_player(player):
    if player: return "X"
    else: return "O"

def iswin(playerA, myBoard):
    if check_row(playerA, myBoard): return True
    if check_col(playerA, myBoard): return True


def check_row(playerA, myBoard):
    for row in myBoard:
        complete_row = True
        for slot in row:
            if slot != playerA:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(playerA, myBoard):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if myBoard[row][col] != playerA:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diagonal(player, myBoard): #checks board from top left of the board to the bottom right of the board in a diagonal direction.
    if myBoard[0][0] == player and myBoard[1][1] == player and myBoard[2][2] == player: return True
    elif myBoard[0][2] == player and myBoard[1][1] == player and myBoard[2][0] == player: return True #checks board from top right of the board to the bottom left of the board in a diagonal direction.

def player(present_player):
    pass


def present_player(numberof_turns=None): #creating present player function consisting of the number of turns the present player gets, which is set to a default value of none.
 while numberof_turns < 9:
    live_user = present_player()
print_myBoard(myBoard)
user_TicTacToe = input("Please enter an X or O")


def live_user(args):
    pass


if quit(user_TicTacToe):
  "break"
  if not check_mark(user_TicTacToe):
    print("Please try again.")
    "continue"
  user_TicTacToe = input(user_TicTacToe)
  coords = coordinates(user_TicTacToe)
  myBoard[0][0] = "O"
  if istaken(coords, myBoard):
    print("Please retry.")
    "continue"
  add_to_myBoard(coords, myBoard)
  if iswin(live_user, myBoard):
      print(f"{live_user.upper()} won!")
"break"
numberof_turns += 1
if numberof_turns == 9: print("Draw")

player = not player

