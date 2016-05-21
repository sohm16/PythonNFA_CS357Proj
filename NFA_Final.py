### THE ALGORITHM
### Recursive. Goes down every path of the NFA's tree. When it reaches the end, tests to see if it accepts.
# lastState = which state to find paths from
# incrementPos = Do I increment position in the string on the next iteration?

def theRecursion(availablePaths, stringPos, lastState, incrementPos, move):
    if len(availablePaths) <= 0: # base case: string is rejected
        if stringPos < len(w) - 1 or lastState not in acceptStates:   # 1- to avoid array out of bounds
            return 'The string was REJECTED.' # string is rejected
        else:
            print('The string was ACCEPTED.') # To implement: stop execution on other branches, we have an accept
            return 'The string was ACCEPTED.'
    else:
        availablePaths = [] # we need to make a new list of paths since we're making a move
        if incrementPos == 1:
            stringPos += 1
        for x in range(0,len(move)): # build a new list of paths
            if (w[stringPos] == move[x][2] or move[x][2] == 'e') and lastState == move[x][0]:
                availablePaths.append(move[x])
        if len(availablePaths) == 0: # hit the end of a tree, just return to test
            return theRecursion(availablePaths, stringPos, lastState, 0, move)
        else:
            for y in range(0, len(availablePaths)):
                if availablePaths[y][2] == 'e': # don't increment string position, used epsilon
                    theRecursion(availablePaths, stringPos, availablePaths[y][1], 0, move) # Don't return to account for branching paths
                else: # return the next state youll be in as well as a command to increment stringPos
                    theRecursion(availablePaths, stringPos, availablePaths[y][1], 1, move) # append accepts / rejects to a list to print off

### GET INPUT STRING & BUILD NFA

runMultiple = 2
while runMultiple != 0: # Run it in a loop so the user can test multiple strings / machines

    if runMultiple == 2:
        print("Please enter your NFA's 5-Tuple.\n")
        numStates = int(input("Total States Q: "))      # Enter # of states: (> 1)
        symbol = input("Symbols in Alphabet Σ: ")       # loop to get all symbols ('e' = epsilon)
        alphabet = [symbol]
        while symbol != "":
            symbol = input("More symbols: ")
            if symbol != "":
                alphabet.append(symbol)
        print("Your alphabet:", alphabet)               # show user alphabet entered
        move = []
        transition = "init"                             # get all transition symbols
        for x in range(0,numStates):
            for y in range(0,numStates):
                transition = "init"
                while transition != "":
                    transition = input("Transition from state " + str(x) + " to state " + str(y) + ": ") # Get transitions between each state
                    if transition != "" and not (x == y and transition == 'e'): # Make sure there are no epsilon transitions to the same state (causes crash, & pointless)
                        move.append([str(x),str(y),transition])
        print("Your transitions:", move)                # show user the transitions they entered
        startState = input("Start State q0: ")
        acceptState = input("Accept States F: ")        # loop to get all accept states
        acceptStates = [acceptState]
        while acceptState != "":
            acceptState = input("More Accept States: ")
            if acceptState != "":
                acceptStates.append(acceptState)
        print("Your accept states:", acceptStates)      # show user acceptStates entered
    w = input("\nString w: ")
    w = w + 'e' # throw an empty symbol on the end to more easily check for an acceptance without crashing
    stringPos = 0 # where we're at on the string while running NFA

    ### RUN w ON THE NFA (Function definition at the top)

    print("If it says the string was ACCEPTED below, then it was accepted. The string was REJECTED otherwise.") # Rather than just shutting down the program..
    # This is a bit more sloppy than sys.exit, but it allows users to enter more than one string without having to restart.
    
    theRecursion(move, stringPos, startState, 0, move) # Run the NFA!
    
    runMultiple = int(input("\nRun again? (0 = No, 1 = New String, 2 = New NFA): ")) # Run as much as user wants
