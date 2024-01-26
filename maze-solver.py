import datetime
from queue import PriorityQueue
import math

def readFile(FILENAME):
    # Opens a text file containing the maze from the subdirectory of the project mazes
    file = open("mazes/" + FILENAME)
    # Reads the file into a matrix
    matrix = []
    # Loops through each line in the file
    for line in file:
        # Removes unwanted spaces and elements that may appear in a file
        line = line.strip()
        if line != "":
            row = line.split(" ")
            last = row.pop()
            if last != "/n":
                row.append(last.strip("/n"))
            if row != []:
                matrix.append(row)
    # Changes the end to a @ to distinguish it from the other positions
    last_line = matrix[len(matrix)-1]
    for i in range(len(last_line)):
        if last_line[i] == "-":
            last_line[i] = "@"
    return matrix

'''Writes the data stored in the matrix into a new/existing file'''
def writeFile(FILENAME, matrix):
    file = open("results/" + FILENAME,"w")
    for line in matrix:
        file.write(''.join(line) + "\n")

'''Gets the starting position of a maze'''
def getStart(matrix):
    for i in range(len(matrix[0])):
        if matrix[0][i] == "-":
            return (0,i)
        
'''Depth-first search to find a solution to the maze input into the programme'''
def depthSearch(FILENAME, matrix):
    # Set up for the search and start position
    moves = [[1,0],[-1,0],[0,-1],[0,1]]
    cords = getStart(matrix)
    finished = False
    nodesVisited = set()
    nodesVisited.add(cords)
    stack = []
    start_time = datetime.datetime.now()
    # The loop that completes the depth search that breaks when it finds a solution
    while not finished:
        matrix[cords[0]][cords[1]] = "~"
        for move in moves:
            new_cords = (cords[0] + move[0] , cords[1] + move[1], cords)
            try:
                # Checks to see if the adjacent nodes are viable to be searched
                if matrix[new_cords[0]][new_cords[1]] == "-":
                    nodesVisited.add(new_cords)
                    stack.append(new_cords)
                elif matrix[new_cords[0]][new_cords[1]] == "@":
                    print('should end')
                    nodesVisited.add(new_cords)
                    stack.append(new_cords)
                    end_time = datetime.datetime.now()
                    finished = True
            except:
                continue

        # Retrieves the next node it must go to
        cords = stack.pop()
        
    # Compares the start and end time to find the time taken    
    time_taken = end_time - start_time
    # Prints the stats of the opperation
    print(time_taken.seconds + time_taken.microseconds / 1000000)
    print(len(nodesVisited))
    # Changes the matrix to show the path found
    length = 0
    loop = True
    while loop == True:
        try:
            matrix[new_cords[0]][new_cords[1]] = "."
            cords = new_cords[2] 
            new_cords = cords
            length = length + 1
        except:
            loop = False
    print(length)
    # Writes the matrix with the nodes visited and the path taken
    writeFile("Depth/"+FILENAME, matrix)


'''Greedy search to find a solution to the maze input into the programme'''
def greedySearch(FILENAME, matrix):
    # Set up for the search and start position
    moves = [[1,0],[-1,0],[0,-1],[0,1]]
    cords = getStart(matrix)
    finished = False
    nodesVisited = set()
    nodesVisited.add(cords)
    priority_queue = PriorityQueue()
    start_time = datetime.datetime.now()
    # Getting cords of the last element to find the distance
    last_line = matrix[len(matrix)-1]
    for i in range(len(last_line)):
        if last_line[i] == "@":
            end_point = (len(matrix)-1,i)
    # The loop that completes the greedy search that breaks when it finds a solution
    while finished == False:
        matrix[cords[0]][cords[1]] = "~"
        for move in moves:
            new_cords = (cords[0] + move[0] , cords[1] + move[1], cords)
            try:
                # Checks to see if the adjacent nodes are viable and add the to a priority 
                # Queue to then be searched later
                if matrix[new_cords[0]][new_cords[1]] == "-":
                    nodesVisited.add(new_cords)
                    # Works out the distance to the end to get the priority
                    distance = int(math.sqrt(((end_point[0] - new_cords[0])**2) \
                                             + ((end_point[1] - new_cords[1])**2)))
                    priority_queue.put( (distance, new_cords) )
                elif matrix[new_cords[0]][new_cords[1]] == "@":
                    print('should end')
                    nodesVisited.add(new_cords)
                    priority_queue.put((0, new_cords))
                    end_time = datetime.datetime.now()
                    finished = True
            except:
                continue    
        cords = priority_queue.get()[1]

    # Compares the start and end time to find the time taken   
    time_taken = end_time - start_time
    # Prints the stats of the opperation
    print(time_taken.seconds + time_taken.microseconds / 1000000)
    print(len(nodesVisited))
    # Changes the matrix to show the path found
    length = 0
    loop = True
    while loop == True:
        try:
            if matrix[new_cords[0]][new_cords[1]] != ".":
                matrix[new_cords[0]][new_cords[1]] = "."
                cords = new_cords[2] 
                new_cords = cords
                length = length + 1
        except:
            loop = False
    print(length)
    # Writes the matrix with the nodes visited and the path taken
    writeFile("Greedy/" + FILENAME, matrix)


# This is where the user will input the file name
FILENAME = "maze-VLarge.txt"

# Runs the two diffrent searches
depthSearch(FILENAME, readFile(FILENAME))
greedySearch(FILENAME, readFile(FILENAME))