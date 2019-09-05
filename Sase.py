from Python_neinformirano_prebaruvanje_final import *


# Check if the white Rook is in a valid position (not in the line of fire of all the black Rooks)
def validityOfWhite(gun, A):
    # print("TESTING WHITE VALIDITY")
    # print(gun)
    location = gun
    # print(location[0] != A[4][0] and location[0] != A[5][0] and location[0] != A[6][0] and location[0] != A[7][0] and
    #        location[1] != A[4][1] and location[1] != A[5][1] and location[1] != A[6][1] and location[1] != A[7][1] and
    #        location[0] < 6 and location[0] > 0 and location[1] > 0 and location[1] < 8)
    return (location[0] != A[4][0] and location[0] != A[5][0] and location[0] != A[6][0] and location[0] != A[7][0] and
            location[1] != A[4][1] and location[1] != A[5][1] and location[1] != A[6][1] and location[1] != A[7][1] and
            location[0] < 6 and location[0] > 0 and location[1] > 0 and location[1] < 8)


# Check if the black Rook is in a valid position (not in the line of fire of all the white Rooks)
def validityOfBlack(gun, A):
    # print("TESTING BLACK VALIDITY")
    # print(gun)
    location = gun
    return (location[0] != A[0][0] and location[0] != A[1][0] and location[0] != A[2][0] and location[0] != A[3][0] and
            location[1] != A[0][1] and location[1] != A[1][1] and location[1] != A[2][1] and location[1] != A[3][1] and
            location[0] < 6 and location[0] > 0 and location[1] > 0 and location[1] < 8)

# Check if the white rooks are not on top of each other
def validityWhiteOnWhite(A):
    return (A[0][0] != A[1][0] and A[0][0] != A[2][0] and A[0][0] != A[3][0] and
            A[1][0] != A[2][0] and A[1][0] != A[3][0] and
            A[2][0] != A[3][0] and
            A[0][1] != A[1][1] and A[0][1] != A[2][1] and A[0][1] != A[3][1] and
            A[1][1] != A[2][1] and A[1][1] != A[3][1] and
            A[2][1] != A[3][1])

# Check if the black rooks are not on top of each other
def validityBlackOnBlack(A):
    return (A[4][0] != A[5][0] and A[4][0] != A[6][0] and A[4][0] != A[7][0] and
            A[5][0] != A[6][0] and A[5][0] != A[7][0] and
            A[6][0] != A[7][0] and
            A[4][1] != A[5][1] and A[4][1] != A[6][1] and A[4][1] != A[7][1] and
            A[5][1] != A[6][1] and A[5][1] != A[7][1] and
            A[6][1] != A[7][1])

class Rooks(Problem):
    def __init__(self, initial):
        self.initial = initial

    def goal_test(self, state):
        return ((state[0] == (5,8) or state[0] == (5,7) or state[0] == (5,6) or state[0] == (5,5)) and
                (state[1] == (5, 8) or state[1] == (5, 7) or state[1] == (5, 6) or state[1] == (5, 5)) and
                (state[2] == (5, 8) or state[2] == (5, 7) or state[2] == (5, 6) or state[2] == (5, 5)) and
                (state[3] == (5, 8) or state[3] == (5, 7) or state[3] == (5, 6) or state[3] == (5, 5)) and
                (state[4] == (1, 1) or state[4] == (1, 2) or state[4] == (1, 3) or state[4] == (1, 4)) and
                (state[5] == (1, 1) or state[5] == (1, 2) or state[5] == (1, 3) or state[5] == (1, 4)) and
                (state[6] == (1, 1) or state[6] == (1, 2) or state[6] == (1, 3) or state[6] == (1, 4)) and
                (state[7] == (1, 1) or state[7] == (1, 2) or state[7] == (1, 3) or state[7] == (1, 4)))

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    def successor(self, state):
        successors = dict()

        WhiteRook1 = state[0]
        WhiteRook2 = state[1]
        WhiteRook3 = state[2]
        WhiteRook4 = state[3]

        BlackRook1 = state[4]
        BlackRook2 = state[5]
        BlackRook3 = state[6]
        BlackRook4 = state[7]
        #
        #
        #
        # WHITE ROOK 1
        #
        #
        #
        # WhiteRook1 UP
        newWhiteRook1 = WhiteRook1
        moves=0
        tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while(validityOfWhite(newWhiteRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook1 = (newWhiteRook1[0], newWhiteRook1[1] - 1)
            moves+=1
            tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook1 = (newWhiteRook1[0], newWhiteRook1[1] + 1)
        stateNew = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook1 - UP'] = stateNew

        # WhiteRook1 DOWN
        newWhiteRook1 = WhiteRook1
        moves = 0
        tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook1 = (newWhiteRook1[0], newWhiteRook1[1] + 1)
            moves += 1
            tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook1 = (newWhiteRook1[0], newWhiteRook1[1] - 1)
        stateNew = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook1 - DOWN'] = stateNew

        # WhiteRook1 LEFT
        newWhiteRook1 = WhiteRook1
        moves = 0
        tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook1 = (newWhiteRook1[0] - 1, newWhiteRook1[1])
            moves += 1
            tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook1 = (newWhiteRook1[0] + 1, newWhiteRook1[1])
        stateNew = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook1 - LEFT'] = stateNew

        # WhiteRook1 RIGHT
        newWhiteRook1 = WhiteRook1
        moves = 0
        tempState = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook1 = (newWhiteRook1[0] + 1, newWhiteRook1[1])
            moves += 1
            tempState = (
            newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook1 = (newWhiteRook1[0] - 1, newWhiteRook1[1])
        stateNew = (newWhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook1 - RIGHT'] = stateNew
        #
        #
        #
        #
        # WHITE ROOK 2
        #
        #
        #
        # WhiteRook2 UP
        newWhiteRook2 = WhiteRook2
        moves = 0
        tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook2 = (newWhiteRook2[0], newWhiteRook2[1] - 1)
            moves += 1
            tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook2 = (newWhiteRook2[0], newWhiteRook2[1] + 1)
        stateNew = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook2 - UP'] = stateNew

        # WhiteRook2 DOWN
        newWhiteRook2 = WhiteRook2
        moves = 0
        tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook2 = (newWhiteRook2[0], newWhiteRook2[1] + 1)
            moves += 1
            tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook2 = (newWhiteRook2[0], newWhiteRook2[1] - 1)
        stateNew = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook2 - DOWN'] = stateNew

        # WhiteRook2 LEFT
        newWhiteRook2 = WhiteRook2
        moves = 0
        tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook2 = (newWhiteRook2[0] - 1, newWhiteRook2[1])
            moves += 1
            tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook2 = (newWhiteRook2[0] + 1, newWhiteRook2[1])
        stateNew = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook2 - LEFT'] = stateNew

        # WhiteRook2 RIGHT
        newWhiteRook2 = WhiteRook2
        moves = 0
        tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook2 = (newWhiteRook2[0] + 1, newWhiteRook2[1])
            moves += 1
            tempState = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook2 = (newWhiteRook2[0] - 1, newWhiteRook2[1])
        stateNew = (WhiteRook1, newWhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook2 - RIGHT'] = stateNew
        #
        #
        #
        #
        # WHITE ROOK 3
        #
        #
        #
        # WhiteRook3 UP
        newWhiteRook3 = WhiteRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(tempState)):
            newWhiteRook3 = (newWhiteRook3[0], newWhiteRook3[1] - 1)
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook3 = (newWhiteRook3[0], newWhiteRook3[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook3 - UP'] = stateNew

        # WhiteRook3 DOWN
        newWhiteRook3 = WhiteRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook3 = (newWhiteRook3[0], newWhiteRook3[1] + 1)
            moves += 1
            tempState = (
            WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook3 = (newWhiteRook3[0], newWhiteRook3[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook3 - DOWN'] = stateNew

        # WhiteRook3 LEFT
        newWhiteRook3 = WhiteRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook3 = (newWhiteRook3[0] - 1, newWhiteRook3[1])
            moves += 1
            tempState = (
            WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook3 = (newWhiteRook3[0] + 1, newWhiteRook3[1])
        stateNew = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook3 - LEFT'] = stateNew

        # WhiteRook3 RIGHT
        newWhiteRook3 = WhiteRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook3 = (newWhiteRook3[0] + 1, newWhiteRook3[1])
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook3 = (newWhiteRook3[0] - 1, newWhiteRook3[1])
        stateNew = (WhiteRook1, WhiteRook2, newWhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook3 - RIGHT'] = stateNew
        #
        #
        #
        #
        # WHITE ROOK 4
        #
        #
        #
        # WhiteRook4 UP
        newWhiteRook4 = WhiteRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook4 = (newWhiteRook4[0], newWhiteRook4[1] - 1)
            moves += 1
            tempState = (
            WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook4 = (newWhiteRook4[0], newWhiteRook4[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook4 - UP'] = stateNew

        # WhiteRook4 DOWN
        newWhiteRook4 = WhiteRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook4 = (newWhiteRook4[0], newWhiteRook4[1] + 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook4 = (newWhiteRook4[0], newWhiteRook4[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook4 - DOWN'] = stateNew

        # WhiteRook4 LEFT
        newWhiteRook4 = WhiteRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook4 = (newWhiteRook4[0] - 1, newWhiteRook4[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook4 = (newWhiteRook4[0] + 1, newWhiteRook4[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook4 - LEFT'] = stateNew

        # WhiteRook4 RIGHT
        newWhiteRook4 = WhiteRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfWhite(newWhiteRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newWhiteRook4 = (newWhiteRook4[0] + 1, newWhiteRook4[1])
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newWhiteRook4 = (newWhiteRook4[0] - 1, newWhiteRook4[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['WhiteRook4 - RIGHT'] = stateNew

        #
        #
        #
        # BLACK ROOK 1
        #
        #
        #
        # BlackRook1 UP
        newBlackRook1 = BlackRook1
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook1 = (newBlackRook1[0], newBlackRook1[1] - 1)
            moves += 1
            tempState = (
            WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newBlackRook1 = (newBlackRook1[0], newBlackRook1[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook1 - UP'] = stateNew

        # BlackRook1 DOWN
        newBlackRook1 = WhiteRook1
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook1 = (newBlackRook1[0], newBlackRook1[1] + 1)
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newBlackRook1 = (newBlackRook1[0], newBlackRook1[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook1 - DOWN'] = stateNew

        # BlackRook1 LEFT
        newBlackRook1 = WhiteRook1
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook1 = (newBlackRook1[0] - 1, newBlackRook1[1])
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newBlackRook1 = (newBlackRook1[0] + 1, newBlackRook1[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook1 - LEFT'] = stateNew

        # BlackRook1 RIGHT
        newBlackRook1 = WhiteRook1
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook1, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook1 = (newBlackRook1[0] + 1, newBlackRook1[1])
            moves += 1
            tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        newBlackRook1 = (newBlackRook1[0] - 1, newBlackRook1[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, newBlackRook1, BlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook1 - RIGHT'] = stateNew
        #
        #
        #
        #
        # BLACK ROOK 2
        #
        #
        #
        # BlackRook2 UP
        newBlackRook2 = BlackRook2
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook2 = (newBlackRook2[0], newBlackRook2[1] - 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        newBlackRook2 = (newBlackRook2[0], newBlackRook2[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook2 - UP'] = stateNew

        # BlackRook2 DOWN
        newBlackRook2 = BlackRook2
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook2 = (newBlackRook2[0], newBlackRook2[1] + 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        newBlackRook2 = (newBlackRook2[0], newBlackRook2[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook2 - DOWN'] = stateNew

        # BlackRook2 LEFT
        newBlackRook2 = BlackRook2
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook2 = (newBlackRook2[0] - 1, newBlackRook2[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        newBlackRook2 = (newBlackRook2[0] + 1, newBlackRook2[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook2 - LEFT'] = stateNew

        # BlackRook2 RIGHT
        newBlackRook2 = BlackRook2
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook2, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook2 = (newBlackRook2[0] + 1, newBlackRook2[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        newBlackRook2 = (newBlackRook2[0] - 1, newBlackRook2[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, newBlackRook2, BlackRook3, BlackRook4)
        successors['BlackRook2 - RIGHT'] = stateNew
        #
        #
        #
        #
        # BLACK ROOK 3
        #
        #
        #
        # BlackRook3 UP
        newBlackRook3 = BlackRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook3 = (newBlackRook3[0], newBlackRook3[1] - 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        newBlackRook3 = (newBlackRook3[0], newBlackRook3[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        successors['BlackRook3 - UP'] = stateNew

        # BlackRook3 DOWN
        newBlackRook3 = BlackRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook3 = (newBlackRook3[0], newBlackRook3[1] + 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        newBlackRook3 = (newBlackRook3[0], newBlackRook3[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        successors['BlackRook3 - DOWN'] = stateNew

        # BlackRook3 LEFT
        newBlackRook3 = BlackRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook3 = (newBlackRook3[0] - 1, newBlackRook3[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        newBlackRook3 = (newBlackRook3[0] + 1, newBlackRook3[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        successors['BlackRook3 - LEFT'] = stateNew

        # BlackRook3 RIGHT
        newBlackRook3 = BlackRook3
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook3, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook3 = (newBlackRook3[0] + 1, newBlackRook3[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        newBlackRook3 = (newBlackRook3[0] - 1, newBlackRook3[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, newBlackRook3, BlackRook4)
        successors['BlackRook3 - RIGHT'] = stateNew
        #
        #
        #
        #
        # BLACK ROOK 4
        #
        #
        #
        # BlackRook4 UP
        newBlackRook4 = BlackRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, newWhiteRook4, BlackRook1, BlackRook2, BlackRook3, BlackRook4)
        while (validityOfBlack(newBlackRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook4 = (newBlackRook4[0], newBlackRook4[1] - 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        newBlackRook4 = (newBlackRook4[0], newBlackRook4[1] + 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        successors['BlackRook4 - UP'] = stateNew

        # BlackRook4 DOWN
        newBlackRook4 = BlackRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        while (validityOfBlack(newBlackRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook4 = (newBlackRook4[0], newBlackRook4[1] + 1)
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        newBlackRook4 = (newBlackRook4[0], newBlackRook4[1] - 1)
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        successors['BlackRook4 - DOWN'] = stateNew

        # BlackRook4 LEFT
        newBlackRook4 = BlackRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        while (validityOfBlack(newBlackRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook4 = (newBlackRook4[0] - 1, newBlackRook4[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        newBlackRook4 = (newBlackRook4[0] + 1, newBlackRook4[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        successors['BlackRook4 - LEFT'] = stateNew

        # BlackRook4 RIGHT
        newBlackRook4 = BlackRook4
        moves = 0
        tempState = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        while (validityOfBlack(newBlackRook4, state) and validityWhiteOnWhite(tempState) and validityBlackOnBlack(
                tempState)):
            newBlackRook4 = (newBlackRook4[0] + 1, newBlackRook4[1])
            moves += 1
            tempState = (
                WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        newBlackRook4 = (newBlackRook4[0] - 1, newBlackRook4[1])
        stateNew = (WhiteRook1, WhiteRook2, WhiteRook3, WhiteRook4, BlackRook1, BlackRook2, BlackRook3, newBlackRook4)
        successors['BlackRook4 - RIGHT'] = stateNew

        return successors


Testing = Rooks(((1,1),(1,2),(1,3),(1,4),(5,5),(5,6),(5,7),(5,8)))
answer = breadth_first_graph_search(Testing)
print (answer.solution())
