import queue

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", " ", "#", "#","#"])
    maze.append(["#"," ", "#", " ", "#", "#","#"])
    maze.append(["#"," ", " ", " ", " ", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def printMaze(path, maze):
    print("printing...")
    for i, pos in enumerate(maze[0]):
        if pos == "O":
            start = i

    xCoord = start
    yCoord = 0
    coords = set()
    for move in path:
        if move == "U":
            yCoord -= 1
        elif move == "D":
            yCoord += 1
        elif move == "L":
            xCoord -= 1
        elif move == "R":
            xCoord += 1

        coords.add((yCoord, xCoord))

    for y, ypos in enumerate(maze):
        for x, xpos in enumerate(maze[y]):
            if (y, x) in coords:
                print("+ ", end="")
            else:
                print(maze[y][x] + " ", end="")
        print()
    print("maze printed.")

def validate(path, maze):
    #invalid if outside maze or crosses over a hash
   print("validating " + str(path))
   for i, pos in enumerate(maze[0]):
        if pos == "O":
            start = i
   
   already_visited = []
   xCoord = start
   yCoord = 0
   for i, move in enumerate(path):
       if move == "U":
           yCoord -= 1
           if ([yCoord, xCoord] in already_visited):
               print("invalid: doubled back")
               return False
           else:
               already_visited.append([yCoord, xCoord])

       elif move == "D":
           yCoord += 1
           if ([yCoord, xCoord] in already_visited):
               print("invalid: doubled back")
               return False
           else:
               already_visited.append([yCoord, xCoord])

       elif move == "L":
           xCoord -= 1
           if ([yCoord, xCoord] in already_visited):
               print("invalid: doubled back")
               return False
           else:
               already_visited.append([yCoord, xCoord])

       elif move == "R":
           xCoord += 1
           if ([yCoord, xCoord] in already_visited):
               print("invalid: doubled back")
               return False
           else:
               already_visited.append([yCoord, xCoord])

       print(yCoord, xCoord, already_visited)

       if not(0 <= yCoord < len(maze[0]) and 0 <= xCoord < len(maze)):
           #print("invalid: exceeded borders")
           return False
       elif (maze[yCoord][xCoord] == "#"):
           #print("invalid: barrier")
           return False

   print("validated")
   return True

def findEnd(path, maze):
    #see if last coordinate is equal to the X
    print("finding end...")
    for i, pos in enumerate(maze[0]):
        if pos == "O":
            start = i

    xCoord = start
    yCoord = 0
    for move in path:
        if move == "U":
            yCoord -= 1
        elif move == "D":
            yCoord += 1
        elif move == "L":
            xCoord -= 1
        elif move == "R":
            xCoord += 1
    if maze[yCoord][xCoord] == "X":
        printMaze(path, maze)
        return True
    return False


nums = queue.Queue()
nums.put("")
maze = createMaze()
addedTo = ""

while not findEnd(addedTo, maze):
    addedTo = nums.get()
    for i in ["U", "D", "L", "R"]:
        toBeQueued = addedTo + i
        if validate(toBeQueued, maze):
            nums.put(toBeQueued)