#creating an array that contains an array, which is an two dimensional array.
myBoard = [
    ["-", "-", "-"], #this is the first index containing an array with a length of three elements
    ["-", "-", "-"], #this is the second index containing an array with a length of three elements
    ["-", "-", "-"] #this is the third index containing an array with a length of three elements
]

def print_myBoard(myBoard): #creating a print myBoard function to print myBoard
    for row in myBoard: #creating for loop for row in myBoard
        for slot in row: #nested for loop for slot in row of myBoard
            print(f"{slot} ", end="") #recognized slot as a predefined variable by using an f string
        print() #prints out a row after a new line

print_myBoard(myBoard)
