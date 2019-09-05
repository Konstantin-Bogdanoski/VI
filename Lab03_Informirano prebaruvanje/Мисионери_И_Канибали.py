from Python_informirano_prebaruvanje import greedy_best_first_graph_search
from Python_informirano_prebaruvanje import Problem

class Mission(Problem):

    def __init__(self,N,capacity):
        self.initial=(N, N, 'L', 0, 0)
        self.capacity=capacity

    def goal_test(self, state):
       if state[0]==0 and state[1]==0:
           return True
       else:
           return False

    def h(self,node):
        missionaryLeft=node.state[0]
        cannibalLeft=node.state[1]

        return (missionaryLeft+cannibalLeft)/2


    def is_valid(self,missionaryLeft, cannibalLeft,missionaryRight, cannibalRight):

        #1. Osiguraj deka Misionerite i Canibalite nema da dobijat negativni vrednosto
        #2. Osiguraj deka Canibalite nemat da gi izedat Misionerite
        if missionaryLeft>=0 and missionaryRight>=0 and cannibalLeft>=0 and cannibalRight>=0 \
        and (missionaryLeft ==0 or missionaryLeft >= cannibalLeft) and ( missionaryRight == 0 or missionaryRight >= cannibalRight): \
            return True
        else:
            return False

    def successor(self, state):
        successors=dict()

        missionaryLeft= state[0]
        cannibalLeft=state[1]
        boat=state[2]
        missionaryRight=state[3]
        cannibalRight=state[4]

        if boat=='L':
            for i in range(1,self.capacity+1):
                for j in range(0, i+1):
                        newMissionaryLeft=missionaryLeft-(i-j)
                        newCannibalLeft=cannibalLeft-j
                        newMissionaryRight=missionaryRight+(i-j)
                        newCannibalRight=cannibalRight+j
                        if(self.is_valid(newMissionaryLeft,newCannibalLeft,newMissionaryRight,newCannibalRight)):
                            successors[str(i-j)+'M_'+str(j)+'K']=(newMissionaryLeft,newCannibalLeft,'D',newMissionaryRight,newCannibalRight)

        if boat=='D':
            for i in range(1,self.capacity+1):
                for j in range(0, i+1):

                        newMissionaryRight = missionaryRight - (i-j)
                        newCannibalRight = cannibalRight - j
                        newMissionaryLeft=missionaryLeft+(i-j)
                        newCannibalLeft=cannibalLeft+j
                        if(self.is_valid(newMissionaryLeft,newCannibalLeft,newMissionaryRight,newCannibalRight)):
                            successors[str(i-j)+'M_'+str(j)+'K']=(newMissionaryLeft,newCannibalLeft,'L',newMissionaryRight,newCannibalRight)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

#main():

N = input()
K = input()

MissionInstance=Mission(int(N),int(K))
answer = greedy_best_first_graph_search(MissionInstance)
print(answer.solve())
