import random

name = "ByteMeBaby"
idlist = []

def moveTo(x , y , Pirate):
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
    
def notCenterorCorner(pirate):
    x,y = pirate.getPosition()
    if (x>15 and x<25) and (y>15 and y<25):
        movexory = random.randint(0,1)
        if movexory == 0:
            if (x-20 > 0):
                return 2
            else: 
                return 4
        else:
            if (y-20 > 0):
                return 3
            else: 
                return 1
    elif (x<10 and y<10):
        movexory = random.randint(0,1)
        if movexory == 0:
            return 2
        else:
            return 3
    elif (x>30 and y<10):
        movexory = random.randint(0,1)
        if movexory == 0:
            return 4
        else:
            return 3
    elif (x>30 and y>30):
        movexory = random.randint(0,1)
        if movexory == 0:
            return 1
        else:
            return 4
    elif (x<10 and y>30):
        movexory = random.randint(0,1)
        if movexory == 0:
            return 1
        else:
            return 2
    else:
        return random.randint(1,4)



def howtomove(pirate):
    x, y = pirate.getPosition()
    z = random.randint(1,9)
    if z < 7 :
        return random.randint(1,4)
    if z > 6:
        return notCenterorCorner(pirate)
    
def gather1(pirate):
    x, y = pirate.getPosition()
    if (y<20):
        if (x != 39 and y%2 == 0):
            return moveTo(39, y, pirate)
        if (x != 0 and y%2 == 1):
            return moveTo(0, y, pirate)
        if (x == 39 or x == 0):
            return moveTo(x, y+1, pirate)
    else:
        if (x != 39 and y%2 == 0):
            return moveTo(39, y, pirate)
        if (x != 0 and y%2 == 1):
            return moveTo(0, y, pirate)
        if (x == 39 or x == 0):
            return moveTo(x, y-1, pirate)
    
def gather2(pirate):
    x, y = pirate.getPosition()
    if (x<20):
        if (y != 39 and x%2 == 0):
            return moveTo(x, 39, pirate)
        if (y != 0 and x%2 == 1):
            return moveTo(x, 0, pirate)
        if (y == 39 or y == 0):
            return moveTo(x+1, y, pirate)
    else:
        if (y != 39 and x%2 == 0):
            return moveTo(x, 39, pirate)
        if (y != 0 and x%2 == 1):
            return moveTo(x, 0, pirate)
        if (y == 39 or y == 0):
            return moveTo(x-1, y, pirate)
    


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    id = int((pirate.getID()))
    idlist.append(id)
    if (id == idlist[0]):
        return gather1(pirate)

    if (id == idlist[1]):
        return gather2(pirate)

    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(s)

    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
        goornot = random.randint(0,1)
        if goornot == 1:
            return moveTo(x, y, pirate)
        else: 
            return howtomove(pirate)
    else:
        return howtomove(pirate)

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    idlist.clear()
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")