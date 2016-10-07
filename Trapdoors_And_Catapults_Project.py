'''
Juan Rios


 Trapdoors & Catapults is a digital version of Chutes & Ladders.

    RULES:

    PLAYERS. There are two players. Humans are prompted for two names, but
    all subsequent action is handled by the program.

    BOARD. The board consists of spaces numbered 0 through 99.

    Ten of the spaces contain a catapult and 10 contain a trapdoor. No space
    contains both a catapult and a trapdoor.

    If a player lands on a catapult, the player is flung forward, possibly as
    far as but not including the winning space (99).

    If a player lands on a trapdoor, the player is dropped back, possibly as far
    as the starting space (0).

    The destination space the player is flung forward to by a catapult or dropped
    back to by a trapdoor never contains a catapult or trapdoor. However, any space
    may be a destination for multiple trapdoors and/or catapults.

    The spaces that contain trapdoors and catapults and the destination of each
    trapdoor and catapult is set at random when the game is set up.

    PLAY. The players begin on space 0. Players move by rolling a die numbered
    1-6. The first to land on space 99 wins.

    The program prints messages telling what happens to each player on each move.
'''

import random

def getPlayerNames():
    print()
    player1 = input('Name of first player: ')
    player2 = input('Name of second player: ')

    '''Return player1 and player2 '''
    return player1, player2


def boardSetup(boardSize, numTrapdoors, numCatapults):

    trapdoors = {} #dictionary 1
    catapults = {} #dictionary 2
    ''' Select trapdoor-destination pairs at random '''
    while len(trapdoors) < numTrapdoors:
        trapdoorSpace = random.randint(1, boardSize-2)
        if trapdoorSpace in trapdoors:
            continue

        ''' Select a destination for this trapdoor. The destination
            must be >= 0 and less than the trapdoorSpace and must not be
            the location of a trapdoor'''
        destination = random.randint(0, trapdoorSpace-1)
        while destination in trapdoors:
            destination = random.randint(0, trapdoorSpace-1)

        ''' Enter the trapdoorSpace-destination pair into the dictionary '''
        trapdoors[trapdoorSpace] = destination

    while len(catapults) < numCatapults:
        catapultsSpace = random.randint(1, boardSize-3)
        if catapultsSpace in catapults:
            continue
        destination = random.randint(catapultsSpace + 1, boardSize - 2)
        while destination in catapults:
            destination = random.randint(catapultsSpace + 1, boardSize - 2)
        catapults[catapultsSpace] = destination

    ''' Returns the trapdoors catapults dictionaries '''
    return trapdoors, catapults

def rollDie():
    ''' Roll a six sided die and return the value of the roll '''
    return random.randint(1, 6)

def switchPlayer(currentPlayer, player1, player2):
    if currentPlayer == player1:
        return player2
    else:
        return player1

def playGame():

    boardSize = 100
    numCatapults = 10
    numTrapdoors = 10

    '''' getPlayerNames() to get names for each of the two players '''
    player1, player2 = getPlayerNames()

    trapdoors, catapults = boardSetup(boardSize, numTrapdoors, numCatapults)
    ''' Initialize the dictionary holding the position of each of the two
        players. keys = players. values = position'''
    position = {player1:0, player2:0}

    ''' Set the initial player '''
    currentPlayer = player1

    ''' Continue play until one player lands on the highest space, and wins '''
    while True:
        print()
        print('Player is', currentPlayer)
        print(currentPlayer, 'is on', position[currentPlayer])
        move = rollDie()
        print(currentPlayer, 'rolls a', move)

        targetPosition = position[currentPlayer] + move

        ''' OVER BOARD SIZE: The roll of the die moves the player beyond
            the end of the board. Print error message. '''
        if targetPosition > boardSize - 1:
            print('Sorry', targetPosition, 'is off the board. No can do,', currentPlayer)

            ''' Switch to the other player '''
            currentPlayer = switchPlayer(currentPlayer, player1, player2)
            continue

        ''' ON THE BOARD: The target position is on the board, so make the move '''
        position[currentPlayer] = targetPosition
        print(currentPlayer, 'moves to', position[currentPlayer])
        currentPlayer = switchPlayer(currentPlayer, player1, player2)


        ''' WINNER: If the current player is on the last
            space, print a WINS! message and break out of the game loop '''
        if position[currentPlayer] == boardSize - 1:
            print(currentPlayer , 'you won!')
            break


        ''' TRAPDOOR: The current player has landed on a trapdoor. Move
            to the trapdoor destination and print out a message. '''
        if position[currentPlayer] in trapdoors:
            position[currentPlayer] = trapdoors[position[currentPlayer]]
            print('Trapdoor!', currentPlayer, 'falls to', position[currentPlayer])

            currentPlayer = switchPlayer(currentPlayer, player1, player2) #swap
            continue

        ''' CATAPULT: If the player has landed on a catapult,
            move to the catapult destination and print out a message. '''
        if position[currentPlayer] in catapults:
            position[currentPlayer] = catapults[position[currentPlayer]]
            print('Catapult!', currentPlayer, 'jumps to', position[currentPlayer])
            currentPlayer = switchPlayer(currentPlayer, player1, player2) # Swap
            continue
playGame()
