import random

name = 'gk'



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
# def ActPirate(pirate):
#     id = int(pirate.getID())
#     try:
#         IdSet.append(id)
#     except NameError:
#         IdSet = [id]
#     x, y = pirate.getPosition() 
#     xD, yD = pirate.getDeployPoint()
#     # a, b, c, d, e, f = , IdSet[1], IdSet[2], IdSet[3], IdSet[4], IdSet[5]
#     #the first pirate go to the first colun, second to second column and so on..
#     if id == IdSet[0]:
#         if (x % 6 != 0):
#             return moveTo(39- xD, y, pirate)
#         else:
#             collectResourceX(pirate, 0)
#     elif id == IdSet[1]:
#         if (x % 6 != 1):
#             return moveTo(39 - xD, y, pirate)
#         else:
#             collectResourceX(pirate, 1)
#     elif id == IdSet[2]:
#         if (x % 6 != 2):
#             return moveTo(39 - xD, y, pirate)
#         else:
#             collectResourceX(pirate, 2)
#     elif id == IdSet[3]:
#         if (x % 6 != 3):
#             return moveTo(39 - xD, y, pirate)
#         else:
#             collectResourceX(pirate, 3)
#     elif id == IdSet[4]:
#         if (x % 6 != 4):
#             return moveTo(39 - xD, y, pirate)
#         else:
#             collectResourceX(pirate, 4)
#     elif id == IdSet[5]:
#         if (x % 6 != 5):
#             return moveTo(39 - xD, y, pirate)
#         else:
#             collectResourceX(pirate, 5)
#     # elif id == IdSet[6]:
#     #     if (y % 6 != 0):
#     #         return moveTo(39 - xD, y, pirate)
#     #     else:
#     #         collectResourceX(pirate, 0)

# def allPiratesInPosition(IdSet):
#     for id in IdSet[:6]:
#         pirate = getPirateById(id)
#         x, y = pirate.getPosition()
#         if x % 6 != id:
#             return False
#     return True

# def ActPirate(pirate):
#     xD, yD = pirate.getDeployPoint()
#     id = int(pirate.getID())
#     try:
#         IdSet.append(id)
#     except NameError:
#         IdSet = [id]
#     x, y = pirate.getPosition() 

#     if id in IdSet[:6]:
#         if x % 6 != id:
#             return moveTo(39 - xD, y, pirate)
#         elif allPiratesInPosition(IdSet):
#             return collectResourceX(pirate, id)
# Global variable to track if all pirates are in position
allPiratesInPosition = False

def ActPirate(pirate):
    global allPiratesInPosition
    xD, yD = pirate.getDeployPoint()
    id = int(pirate.getID())
    try:
        IdSet.append(id)
    except NameError:
        IdSet = [id]
    x, y = pirate.getPosition() 

    if id in IdSet[:6]:
        if x % 6 != id:
            # Move to the target row
            return moveTo(x, 39-yD, pirate)
        else:
            # If all pirates are in position, start collecting resources
            if allPiratesInPosition:
                return collectResourceX(pirate, id)
            # If not all pirates are in position, check if this pirate is the last one to reach its row
            elif id == max(IdSet[:6]):
                allPiratesInPosition = True
def ActTeam(team):
    pass