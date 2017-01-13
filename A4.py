#Author: Jeffrey Shen
#ID: 10153021
#Tutorial: T04
#This program is a game that that allows for the user to manually change the player's location
#The Taminator is a random event that can be generated in the game, and accelerates the time by 2 turns when adjacent to the player
#The Taminator is able to track the player's location and move towards it
#The Pavol is also a randomly generated event that pauses the number of turns
#The student's object is to collect "w" to increase their GPA counter, or "f" to increase their fun counter
#A program limitation is that you cannot simultaneously generate two random events at the same time. There can only be one random event
#generated at a given time.

import random

SIZE = 10
STUDENT = "S"
WORK = "w"
FUN = "f"
TAMINATOR = "T"
EMPTY = " "

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @display()
# @Argument: a reference the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: Mone
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# '''
def display(world):
    for r in range (0, SIZE, 1):
    # Row of dashes before each row
        for i in range (0, SIZE, 1):
            print(" -", end="")
        print()
        for c in range (0, SIZE, 1):
            # Vertical bar before displaying each element
            print("|" + world[r][c], end="")
        print("|") # Vertical bar right of last element + CR to
		           # move output to the next line

    # A line of dashes before each row, one line after the last
    # row.
    for i in range (0, SIZE, 1):
        print(" -", end="")
    print()
# @getChoice()
# @Argument: None
# @Return: Returns integer to choice
# @ This function gets input from the user for which direction to move the player
def getChoice():
    print("MOVEMENT TYPES")
    print("7 8 9 \n4 5 6 \n1 2 3")
    print("Type a number on the key pad to indicate direction of movement \nType 5 to pass on movement.")
    while True:
        try:
            choice = int(input("Selection:"))
            valid = True
        except:
            print("Please enter an integer.")
        try:
            assert choice >= 0 and choice <10
            break
        except AssertionError:
            print("Please enter a number on the key pad.")
    return choice

# @getPosition()
# @Argument: A reference to the 2D list which is the game world
# @Return: Returns an integer to row and col
# @ This function scans the 2D game world list and indexes for the list
# @ element that corresponds to the location of the STUDENT. The corresponding list index
# @ for the 2D list is then returned as coordinates for the STUDENT
def getPosition(world):
    row = -1
    column = -1
    for r in range (len(world)):
        for c in range (len(world[r])):
            if world[r][c] == STUDENT:
                row = r
                col = c
    assert row != -1 and col != -1
    return row, col

# @getCheat()
# @Argument: None
# @Return: Returns string to cheatChoice
# @ This function gets input from the user for which cheat option to choose
def getCheat():
    print("Cheat menu options")
    print("(t)oggle debug mode on")
    print("(m)ake the Taminator appear")
    print("(q)uit cheat menu")
    cheatChoice = input("Enter cheat selection:")
    return cheatChoice

# @getTamPosition()
# @Argument: None
# @Return: Returns an integer to row and to column
# @ This function gets input from the user to set where the TAMINATOR appears
# @ on the game map.
def getTamPosition():
    print("Enter a row 0-9:", end="")
    row = int(input())
    print("Enter a column 0-9:", end="")
    column = int(input())
    return (row, column)

# @locateTam()
# @Argument: A reference to the 2D list which is the game world
# @Return: Returns an integer to row and to col
# @ This function scans the 2D game world list and indexes for the list
# @ element that corresponds to the location of the TAMINATOR. The corresponding list index
# @ for the 2D list is then returned as coordinates for the TAMINATOR
def locateTam(world):
    row = -1
    column = -1
    for r in range (len(world)):
        for c in range (len(world[r])):
            if world[r][c] == TAMINATOR:
                row = r
                col = c
    assert row != -1 and col != -1
    return row, col

# @locateRandTam()
# @Argument: A reference to the 2D list which is the game world
# @Return: Returns a random integer from 0-9 and sets to row and column
# @ This function generates a random integer from 0-9 and sets it to row,
# @ and then it generates another random integer from 0-9 and sets it to column
def locateRandTam(world):
    row = random.randrange(0,10)
    column = random.randrange(0,10)
    return row, column


# @finalStats()
# @Argument: takes an integer value for gpa and integer value for fun
# @Return: Returns GPA converted to a letter grade (string)
# @ This function converts gpa into a letter grade
def finalStats(gpa,fun):
    if gpa == 0:
        gpa = "F"
    elif gpa == 1:
        gpa = "D"
    elif gpa == 2:
        gpa = "C"
    elif gpa == 3:
        gpa = "B"
    elif gpa == 4:
        gpa = "A"
    return ("GPA = %s" % gpa)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# This function was slightly modified for personal readability
# @ This function works in conjunction with readFromFile()
# @intialize()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element
# @is set to an exclamation mark).
# '''
def initialize():
    world = []
    for r in range (SIZE):
        r = []
        for c in range (SIZE):
            r.append ("!")
        world.append(r)
    return world
# Author:  James Tam
# @ This method works in conjunction with initialize. Initialize creates
# @ the list with list elements containing a default value '!'. This method
# @ relies on the list already being created and sets each list element to
# @ a corresponding value read in from the input file e.g. the string at
# @ row 2 and column 4 in the input file will initialize the list element
# @ at this same location in the 2D list (game world).
# @readFromFile()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element
# @will now be initialized to the values read in from the input file
# '''
def readFromFile():
    r = -1
    c = -1
    world = initialize() # Needed to create the 2D list
    inputFilename = input("Name of input file: ")

    try:
        inputFile = open(inputFilename,"r")
        r = 0
        # Read one line at a time from the file into a string
        for line in inputFile:
            c = 0
            # Iterate 1 char at a time through the string
            for ch in line:
                # Including EOL there's 11 characters per line
                # 10x10 list , exclude the EOL to avoid reading
                # outside the bounds of the list (10 columns)
                if (c < SIZE):
                    # Set list element to the single char
                    # read from file
                    world[r][c] = ch
                    # Advance to next element along row
                    c = c + 1
                # Entire row has been set to values read in from
                # file, move to next row
            r = r + 1
        inputFile.close()
    except IOError:
        print("Error reading from " + inputFilename)
    return(world)

#################################################################
# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
def start():
    pavolSelected = False
    tamSelected = False
    tamRandSelected = False
    turns = 13
    gpa = 0
    fun = 0
    debugOn = False
    world = readFromFile()
    while turns>0:
        if tamSelected or tamRandSelected and tamTurns > 0:
            currRow, currCol = getPosition(world)
            currRowTam, currColTam = locateTam(world)
            if (currRow - currRowTam > 2):
                newRowTam = currRowTam +2
            elif (currRow - currRowTam < -2):
                newRowTam = currRowTam - 2
            elif (currRow - currRowTam == 2):
                newRowTam = currRowTam +2
            elif (currRow - currRowTam == -2):
                newRowTam = currRowTam - 2
            else:
                newRowTam = currRowTam +(currRow - currRowTam)

            if (currCol - currColTam > 2):
                newColTam = currColTam + 2
            elif (currCol - currColTam < -2):
                newColTam = currColTam - 2
            elif (currCol - currColTam == 2):
                newColTam = currColTam + 2
            elif (currCol - currColTam == -2):
                newColTam = currColTam - 2
            else:
                newColTam = currColTam +(currCol - currColTam)

            if world[newRowTam][newColTam] == FUN:
                if debugOn:
                    print("<<The Taminator has moved onto a \"f\".>>")
                world[newRowTam][newColTam] = TAMINATOR
                world[currRowTam][currColTam] = EMPTY
            elif world[newRowTam][newColTam] == WORK:
                if debugOn:
                    print("<<The Taminator has moved onto a \"w\".>>")
                world[newRowTam][newColTam] = TAMINATOR
                world[currRowTam][currColTam] = EMPTY
            elif world[newRowTam][newColTam] == STUDENT:
                if (currRow - currRowTam == 2):
                    newRowTam = newRowTam -1
                elif (currRow - currRowTam == -2):
                    newRowTam = newRowTam +1
                else:
                    newRowTam = currRowTam
                if (currCol - currColTam == 2):
                    newColTam = newColTam -1
                elif (currCol - currColTam == -2):
                    newColTam = newColTam +1
                else:
                    newColTam = currColTam
                world[currRowTam][currColTam] = EMPTY
                world[newRowTam][newColTam] = TAMINATOR

            else:
                world[newRowTam][newColTam] = TAMINATOR
                world[currRowTam][currColTam] = EMPTY
                if debugOn:
                    print("<<The Taminator has moved onto an empty space.>>")
            tamTurns = tamTurns - 1
            if tamTurns >0:
                if (world[newRowTam][newColTam+1] == STUDENT) or \
                (world[newRowTam][newColTam-1] == STUDENT) or \
                (world[newRowTam+1][newColTam] == STUDENT) or \
                (world[newRowTam-1][newColTam] == STUDENT) or \
                (world[newRowTam-1][newColTam-1] == STUDENT) or \
                (world[newRowTam-1][newColTam+1] == STUDENT) or \
                (world[newRowTam+1][newColTam-1] == STUDENT) or \
                (world[newRowTam+1][newColTam+1] == STUDENT):
                    turns = turns -2
                    if debugOn:
                        print("<<If the Taminator is adjacent to the Player, you will see this message and the game will advance time by an additional 2 turns.>>")
            if tamTurns == 0:
                world[newRowTam][newColTam] = EMPTY
                tamSelected = False
                tamRandSelected = False

        print("current turns = %d" % turns)
        print("GPA = %d" % gpa)
        print("Fun Points = %d" % fun)
        display(world)
        try:
            choice = getChoice()
        except:
            print("Please enter a valid choice.")
        currRow, currCol = getPosition(world)
        if choice == 9:
            newRow, newCol = currRow-1, currCol+1
        elif choice == 8:
            newRow, newCol = currRow-1, currCol
        elif choice == 7:
            newRow, newCol = currRow-1, currCol-1
        elif choice == 6:
            newRow, newCol = currRow, currCol+1
        elif choice == 5:
            newRow, newCol = currRow, currCol
        elif choice == 4:
            newRow, newCol = currRow, currCol-1
        elif choice == 3:
            newRow, newCol = currRow+1, currCol+1
        elif choice == 2:
            newRow, newCol = currRow+1, currCol
        elif choice == 1:
            newRow, newCol = currRow+1, currCol-1
        elif choice == 0:
            newRow, newCol = currRow, currCol
            cheatChoice = getCheat()
            if cheatChoice == "t":
                if debugOn:
                    debugOn = False
                    print("Debug mode is off")
                else:
                    debugOn = True
                    print("Debug mode is on.")
            elif cheatChoice == "m":
                tamSelected = True
                tamTurns = 3
                currRowTam, currColTam = getTamPosition()
                print("\nBeware the Taminator is here.")
                world[currRowTam][currColTam] = TAMINATOR
                display(world)
            elif cheatChoice == "q":
                print()
        try:
            if world[newRow][newCol] == FUN:
                fun = fun+1
                turns = turns-1
                world[newRow][newCol] = STUDENT
                world[currRow][currCol] = EMPTY
                if debugOn:
                    print("<<Player has moved to a location where a \"f\" resides, and subsequently increased the FUN points counter by 1.>>")
            elif world[newRow][newCol] == WORK:
                gpa = gpa +1
                turns = turns-1
                world[newRow][newCol] = STUDENT
                world[currRow][currCol] = EMPTY
                if debugOn:
                    print("<<Player has moved to a location where a \"w\" resides, and subsequently increased the GPA counter by 1.>>")
            elif world [newRow][newCol] == TAMINATOR:
                print("You cannot move onto the Taminator.")
                if debugOn:
                    print("<<Player has attempted to move to where \"T\" resides.>>")
            else:
                world[currRow][currCol] = EMPTY
                world[newRow][newCol] = STUDENT
                turns = turns-1
                if debugOn:
                    print("<<Player has moved to an empty location or remained at the same location.>>")
        except IndexError:
            print("\nYou're going out of bounds!")
        # except UnboundLocalError:
        #     print("\nYou must enter a number on the num pad.")

        if pavolSelected and pavolTurns > 0:
            turns = turns + 1
            pavolTurns = pavolTurns - 1
            if pavolTurns == 0:
                pavolSelected = False


        elif not tamSelected and not tamRandSelected:
            pavol = random.randrange(1,11)
            if pavol == 1:
                pavolSelected = True
                pavolTurns = 1
                print("Pavol appears and stops time momentarily...")
                turns = turns + 1

        if not pavolSelected and not tamRandSelected and not tamSelected:
            tam = random.randrange(1,5)
            if tam == 1:
                print("The Taminator Appears!!!")
                tamRandSelected = True
                tamTurns = 3
                currRowTam, currColTam = locateRandTam(world)
                world[currRowTam][currColTam] = TAMINATOR
                display(world)

    a = finalStats(gpa,fun)
    try:
        fileOut = open("stats.txt", "w")
        print(a, file=fileOut)
    except:
        print("Some error occured, please check your current location.")

start()
