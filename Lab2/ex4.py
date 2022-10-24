def calculatePosition(actualIndex: int, numberToAdd:int, arrayLength:int):
    if numberToAdd > 0:
        numberToAdd %= arrayLength
    elif numberToAdd < 0:
        numberToAdd *= -1 # making it positive
        numberToAdd %= arrayLength # applying the abs
        numberToAdd *= -1 # making it back negative
        numberToAdd += arrayLength # making it back positive but smaller than the array length
    else:
        return actualIndex
    while numberToAdd != 0:
        if (actualIndex + numberToAdd) < arrayLength: # the sum does not exceed
            actualIndex = actualIndex + numberToAdd
            numberToAdd = 0
        elif (actualIndex + numberToAdd) == arrayLength: # the sum is the length itself
            actualIndex = 0
            numberToAdd = 0
        elif (actualIndex + numberToAdd) > arrayLength: # the sum exceeds
            actualIndex = (actualIndex + numberToAdd) - arrayLength
            numberToAdd = 0
    return actualIndex

def compose(notes: str, moves: int, startingPosition: int):
    result: str = []
    index: int = startingPosition
    result.append(notes[startingPosition]) # the first note has to be the starting position
    for x in range(0, len(moves)):
        index = calculatePosition(index, moves[x], len(notes)) # the new index after adding the move
        result.append(notes[index])
    return result

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))