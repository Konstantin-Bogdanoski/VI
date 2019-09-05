from Python_informirano_prebaruvanje import *
from Python_neinformirano_prebaruvanje_final import *

def clickOnPosition(position, state):
    tempState = list()

    for i in state:
        tempRow = list(i)
        tempState.append(tempRow)

    for i in range(len(state)):
        tempRow = list(state[i])
        for j in range(len(tempRow)):
            if(position[0] == i and position[1] == j):
                tempState[i][j] = tempState[i][j] * (-1)
                if(i != 0):
                    tempState[i - 1][j] = tempState[i-1][j] * (-1)
                if(i < len(state) - 1):
                    tempState[i + 1][j] = tempState[i + 1][j] * (-1)
                if(j != 0):
                    tempState[i][j - 1] = tempState[i][j - 1] * (-1)
                if(j < len(tempRow) - 1):
                    tempState[i][j + 1] = tempState[i][j + 1] * (-1)

    theTuple = list()
    for i in tempState:
        tempRow = tuple(i)
        theTuple.append(tempRow)

    return tuple(theTuple)

class Clicks(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        for i in state:
            for j in i:
                if(j == -1):
                    return False
        return True

    def successor(self, state):
        successors = dict()
        for i in range(len(state)):
            tempRow = state[i]
            for j in range(len(tempRow)):
                tempState = clickOnPosition([i,j],state)
                successors["x: " + str(i) + " | y: " + str(j)] = tempState
        return successors

    def h(self, node):
        count = 0
        for i in self.initial:
            for j in i:
                if(j==1):
                    count += 1
        return count

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]



N = int(input())
polinja = list(map(int, input().split(',')))
#polinja = input().split(",")

matrix=list()
goalMatrix=list()
k=0

for i in range(N):
    row=[]
    goalRow=[]
    for j in range(N):
        row.append(polinja[k])
        goalRow.append(1)
        k+=1
    matrix.append(tuple(row))
    goalMatrix.append(tuple(goalRow))


myMatrix = tuple(matrix)
myGoal = tuple(goalMatrix)
#print(matrix)


problem = Clicks(myMatrix, myGoal)
answer = astar_search(problem)
print (answer)
print(answer.solution())