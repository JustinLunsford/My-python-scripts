import random




player = 'player'
cpu = 'computer'

#This code is largely the same because I over-engineered the original and already exceeded the criteria for this one.
#Oops.

#However I added like a handful of small changes and fixed a small but annoying bug where the bot would
#overwrite the 0 index of the board if it was the most viable option, regardless of whether or not the
#space was already filled.


board = []

def makeBoard() -> []:
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def printBoard(currentMove: str, board: []):
    print("\n" + currentMove + ":\n" +
        str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + "\n---------\n" +
          str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + "\n---------\n" +
          str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + "\n")




def getPlayerMove(board: []) -> int:
    looking = True
    while (looking):
        playerIndex = int(input("What slot do you want to fill in?(numerically)\n>>> "))
        if (0 < playerIndex < 10):
            if (board[playerIndex - 1].isdigit()):
                return playerIndex - 1
            else:
                print("That space is already filled in.")
        else:
            print("That space does not exist.")


def getComputerMove(board: []) -> int:
    looking = True
    while (looking):
        indexNum = random.randint(0, len(board) - 1)
        if (board[indexNum].isdigit()):
            return indexNum
def getComputerMoveHard(board: [], myInput: str) -> int:
    firstPick = True
    for piece in board:
        if (piece.isdigit() == False):
            firstPick = False
            break
    if (firstPick):
        return random.randint(0, len(board) - 1)
    
    #checks the viability of every win condition
    diagViability = diagStrat(board, myInput)
    vertViability = vertStrat(board, myInput)
    horViability = horizonStrat(board, myInput)
    viabilities = [diagViability, vertViability, horViability]
    
    #checks the viability of every viable win condition and finds the best among them, and uses that to pick out a piece to fill
    highestViability = 0
    hIndex = 0
    for vb in viabilities:
        if (vb[0] > highestViability):
            highestViability = vb[0]
            hIndex = vb[1]
    #debug check to make sure the bot will not override an existing check
    if (board[hIndex] == 'X' or board[hIndex] == 'O'):
        #if the space the bot decided on is already filled, it will instead grab the first available space
        #as a failsafe
        firstAvailable = 0
        for space in board:
            if (space != 'X' and space != 'O'):
                hIndex = firstAvailable
            else:
                firstAvailable += 1
    return hIndex


def diagStrat(board: [], myInput: str) -> []:
    
    #Checks the viability of both diagonal win conditions and returns the higher of the two as well as the best index from it
    btDiag = [board[0], board[4], board[8]]
    tbDiag = [board[2], board[4], board[6]]
    
    btViability = checkViability(btDiag, myInput)
    tbViability = checkViability(tbDiag, myInput)
    if (btViability[0] >= tbViability[0]):
        return btViability
    else:
        return tbViability
    
def vertStrat(board: [], myInput: str) -> []:
    
    #Checks the viability of every vertical win condition and returns the highest as well the best index from it
    lcVert = [board[0], board[3], board[6]]
    mcVert = [board[1], board[4], board[7]]
    rcVert = [board[2], board[5], board[8]]
    
    lcVia = checkViability(lcVert, myInput)
    mcVia = checkViability(mcVert, myInput)
    rcVia = checkViability(rcVert, myInput)
    
    viabilities = [lcVia, mcVia, rcVia]
    highestIndex = 0
    highestVia = 0
    currentIndex = -1
    for strat in viabilities:
        currentIndex += 1
        if (strat[0] > highestVia):
            highestVia = strat[0]
            highestIndex = currentIndex
    return viabilities[highestIndex]

def horizonStrat(board: [], myInput: str) -> []:
    
    #Checks the viability of every horizontal win condition and returns the highest as well as the best index from it
    tcHor = [board[0], board[1], board[2]]
    mcHor = [board[3], board[4], board[5]]
    bcHor = [board[6], board[7], board[8]]
    
    tcVia = checkViability(tcHor, myInput)
    mcVia = checkViability(mcHor, myInput)
    bcVia = checkViability(bcHor, myInput)
    
    viabilities = [tcVia, mcVia, bcVia]
    highestIndex = 0
    highestVia = 0
    currentIndex = -1
    for strat in viabilities:
        currentIndex += 1
        if (strat[0] > highestVia):
            highestVia = strat[0]
            highestIndex = currentIndex
    return viabilities[highestIndex]

def checkViability(strat: [], myInput: str) -> []:
    #returns a list of two ints, one being its viability the other being a possible index
    #for every blank space found is +1 viability, and for every existing CPU input is +2 viability, the highest
    #viability possible would be 7, which if found is an instant win for the CPU
    viability = 0
    possibleIndex = 0
    for space in strat:
        if (space.isdigit()):
            viability += 1
            possibleIndex = int(space) - 1
        elif (space == myInput):
            viability += 3
        else:
            viability -= 10
            
    #A viability of -19 would mean that the player only needs one more turn to fill in a final space, and the bot
    #will prevent that
    if (viability == 7):
        viability = 20
    elif (viability == -19):
        viability += 30
    return [viability, possibleIndex]

def checkForWinner(board: [], inputCheck : str):
    emptySpaceFound = False
    for check in board:
        if (check.isdigit()):
            emptySpaceFound = True
            break
        
    if (checkDiag(board, inputCheck) or checkHorizon(board, inputCheck)
        or checkVert(board, inputCheck)):
        return 'Win'
        
    else:
        if (emptySpaceFound):
            return 'keep playing'
        else:
            return 'tie'

def checkDiag(board: [], inputCheck: str) -> bool:
    if (board[0] == inputCheck and board[4] == inputCheck and board[8] == inputCheck):
        return True
    elif (board[2] == inputCheck and board[4] == inputCheck and board[6] == inputCheck):
        return True
    else:
        return False
    
def checkHorizon(board: [], inputCheck : str) -> bool:
    if (board[0] == inputCheck and board[1] == inputCheck and board[2] == inputCheck):
        return True
    elif (board[3] == inputCheck and board[4] == inputCheck and board[5] == inputCheck):
        return True
    elif (board[6] == inputCheck and board[7] == inputCheck and board[8] == inputCheck):
        return True
    else:
        return False
def checkVert(board: [], inputCheck: str) -> bool:
    if (board[0] == inputCheck and board[3] == inputCheck and board[6] == inputCheck):
        return True
    elif (board[1] == inputCheck and board[4] == inputCheck and board[7] == inputCheck):
        return True
    elif (board[2] == inputCheck and board[5] == inputCheck and board[8] == inputCheck):
        return True
    else:
        return False

botWins = 0
playerWins = 0
currentRound = 1
hard = bool

if __name__ == '__main__':
    playing = True
    while (playing):
        if (currentRound == 1):
            print('Welcome to Tic-Tac-Toe!')
            hardMode = input("Easy or hard mode?(e/h)\n>>> ")
            if (hardMode == "h"):
                hard = True
            else:
                hard = False
        else:
            print("Round " + str(currentRound) + "!")
        # Ask the player what team they want to be.
        playerTeam = input('Do you want to be X or O?\n>>> ').upper()
    
    
        if playerTeam == 'X':
            computerTeam = 'O'
        elif playerTeam == 'O':
            computerTeam = 'X'
        else:
            print("Invalid. You're O by default.")
            playerTeam = 'O'
            computerTeam = 'X'
        whoseTurn = str
        if (hard):
            whoseTurn = cpu
        else:
            whoseTurn = random.choice([player, cpu])
        print('The {} will go first.'.format(whoseTurn))
    
    
        # Get a fresh board.
        board = makeBoard()
        matchGoing = True
        while matchGoing:
            if whoseTurn == player:
                printBoard("Current board", board)
                index = getPlayerMove(board)
                board[index] = playerTeam
            else:
                if (hard):
                    index = getComputerMoveHard(board, computerTeam)
                else:
                    index = getComputerMove(board)
                board[index] = computerTeam
                printBoard(whoseTurn, board)
            inputCheck = str
            if (whoseTurn == "player"):
                inputCheck = playerTeam
            else:
                inputCheck = computerTeam
                
            winStatus = checkForWinner(board, inputCheck)
            if winStatus != 'keep playing':
                if winStatus == 'tie':
                    print('-------------------')
                    print("It's a tie!")
                    printBoard("Final board", board)
                else:
                    print('-------------------')
                    print('The {} wins!'.format(whoseTurn))
                    printBoard("Final board", board)
                    if (whoseTurn == player):
                        playerWins += 1
                    else:
                        botWins += 1
                matchGoing = False
                playAgain = input("A great match from the both of you. Would you like to play again?(y/n)\n>>> ")
                if (playAgain != "y"):
                    playing = False          
                    print("\nFINAL SCORE\n-----------\nPlayer: " + str(playerWins) + "\nComputer: " + str(botWins))
                currentRound += 1
    
            if whoseTurn == player:
                whoseTurn = cpu
            else:
                whoseTurn = player