import random

name = 'gk'

IdSet = list()
collectingPirateIdY = {}
collectingPirateIdX = {}


def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1


def moveStraight(direction, pirate):
    if direction == "n":
        return 1
    if direction == "s":
        return 3
    if direction == "e":
        return 2
    if direction == "w":
        return 4

def collectResourceX(pirate, lambda_):
    x, y = pirate.getPosition()
    xD, yD = pirate.getDeployPoint()
    xD += lambda_
    yD += lambda_

    # First quadrant deploy point
    if (xD < 20 and yD < 20):
        if (((y - yD) % 6)) < 3:
            if x != 39: return moveStraight('e', pirate)
            else: return moveStraight('s', pirate)
        else:
            if x != 0: return moveStraight('w', pirate)
            else: return moveStraight('s', pirate)

    # Second quadrant deploy point
    elif (xD >= 20 and yD < 20):
        if (((y - yD) % 6)) < 3:
            if x != 0: return moveStraight('w', pirate)
            else: return moveStraight('s', pirate)
        else:
            if x != 39: return moveStraight('e', pirate)
            else: return moveStraight('s', pirate)

    # Third quadrant deploy point
    elif (xD >= 20 and yD >= 20):
        if (((y - yD) % 6)) < 3:
            if x != 0: return moveStraight('w', pirate)
            else: return moveStraight('n', pirate)
        else:
            if x != 39: return moveStraight('e', pirate)
            else: return moveStraight('n', pirate)

    # Fourth quadrant deploy point
    elif (xD < 20 and yD >= 20):
        if (((y - yD) % 6)) < 3:
            if x != 39: return moveStraight('e', pirate)
            else: return moveStraight('n', pirate)
        else:
            if x != 0: return moveStraight('w', pirate)
            else: return moveStraight('n', pirate)

def collectResourceY(pirate, lambda_):
    x, y = pirate.getPosition()
    xD, yD = pirate.getDeployPoint()
    xD += lambda_
    yD += lambda_

    # First quadrant deploy point
    if (xD < 20 and yD < 20):
        if (x - xD) % 6 < 3:
            if y != 39: return moveStraight('s', pirate)
            else: return moveStraight('e', pirate)
        else:
            if y != 0: return moveStraight('n', pirate)
            else: return moveStraight('e', pirate)

    # Second quadrant deploy point
    elif (xD >= 20 and yD < 20):
        if (x - xD) % 6 < 3:
            if y != 39: return moveStraight('s', pirate)
            else: return moveStraight('w', pirate)
        else:
            if y != 0: return moveStraight('n', pirate)
            else: return moveStraight('w', pirate)

    # Third quadrant deploy point
    elif (xD >= 20 and yD >= 20):
        if (x - xD) % 6 < 3:
            if y != 0: return moveStraight('n', pirate)
            else: return moveStraight('w', pirate)
        else:
            if y != 39: return moveStraight('s', pirate)
            else: return moveStraight('w', pirate)

    # Fourth quadrant deploy point
    elif (xD < 20 and yD >= 20):
        if (x - xD) % 6 < 3:
            if y != 0: return moveStraight('n', pirate)
            else: return moveStraight('e', pirate)
        else:
            if y != 39: return moveStraight('s', pirate)
            else: return moveStraight('e', pirate)
def moveToRow(pirate, lambda_):
    x, y = pirate.getPosition()

    # Calculate the nearest row
    r_up = y - y % 3 + lambda_
    if r_up < y:
        r_up += 3

    r_down = y - y % 3 + lambda_
    if r_down > y:
        r_down -= 3

    # Choose the nearest row
    r = r_up if abs(r_up - y) < abs(r_down - y) else r_down

    # Move the pirate towards the target row
    if y < r and y < 39:  # Ensure the pirate doesn't move out of bounds
        return moveStraight('s', pirate)
    elif y > r and y > 0:  # Ensure the pirate doesn't move out of bounds
        return moveStraight('n', pirate)
    else:
        # If the pirate is already on the target row, do nothing
        return 0  
def ActPirate(pirate):
    # complete this function
    id = int(pirate.getID())
    IdSet.append(id)
    x,y = pirate.getPosition() 
    if (pirate.getCurrentFrame() == 1):
        return moveTo(x, 39 - y, pirate) if id in IdSet[:4] else moveTo(39 - x, y, pirate)
    if (pirate.getCurrentFrame() == 2):
        if (id == IdSet[0]):    return moveToRow(pirate,1)
        if (id == IdSet[1]):    return moveToRow(pirate,2)
        if (id == IdSet[2]):    return moveToRow(pirate,0)

        if (id == IdSet[3]):    return moveToRow(pirate,1)
        if (id == IdSet[4]):    return moveToRow(pirate,2)
        if (id == IdSet[5]):    return moveToRow(pirate,0)

    if (pirate.getCurrentFrame() >= 3):
        if (id == IdSet[0]):    return collectResourceX(pirate, 1)
        if (id == IdSet[1]):    return collectResourceX(pirate, 2)
        if (id == IdSet[2]):    return collectResourceX(pirate, 0)

        if (id == IdSet[3]):    return collectResourceY(pirate, 1)
        if (id == IdSet[4]):    return collectResourceY(pirate, 2)
        if (id == IdSet[5]):    return collectResourceY(pirate, 0)

    # print(collectingPirateIdX)
        