CoveceRedica = input()
CoveceKolona = input()
KukaRedica = input()
KukaKolona = input()
from Python_informirano_prebaruvanje import Problem
from Python_informirano_prebaruvanje import astar_search
from Python_informirano_prebaruvanje import recursive_best_first_search
coordinates = {0:(CoveceRedica,CoveceKolona),1:(KukaRedica,KukaKolona)}

def updateDigi(P):
    X, Y ,Nasoka = P
    if ((Y == 0 and Nasoka == -1) or (X == 4 and Nasoka == 1)\
    and (Y==4 and Nasoka==-1) or (X==10 and Nasoka==1)):
        Nasoka = Nasoka * (-1)
    Ynew = Y + Nasoka
    Xnew = X + Nasoka
    Pnew = Xnew ,Ynew , Nasoka
    return Pnew

def updateVert(P):
    X, Y, Nasoka = P
    if(X==5 and Nasoka==-1) or (X==9 and Nasoka==1):
        Nasoka = Nasoka * (-1)
    Xnew = X + Nasoka
    Pnew = Xnew , Y , Nasoka
    return Pnew

def updateHori(P):
    X ,Y, Nasoka = P
    if(Y==0 and Nasoka==-1) or (Y==4 and Nasoka==1):
        Nasoka = Nasoka * (-1)
    Ynew = Y + Nasoka
    Pnew = X , Ynew , Nasoka
    return Pnew

def mhd(n ,m):
    CoveceRedica ,CoveceKolona = coordinates[n]
    KukaRedica ,KukaKolona = coordinates[m]
    return abs(int(CoveceRedica) - int(KukaRedica))+abs(int(CoveceKolona) - int(KukaKolona))


class Istrazhuvach(Problem):

    def __init__(self,initial ,goal):
        self.initial = initial
        self.goal = goal


    def goal_test(self, state):
        g = self.goal
        return (state[0] == g[0] and state[1] == g[1])

    def h(self ,node):
        return mhd(0,1)

    def successor(self, state):
        successors = dict()
        X=state[0]
        Y=state[1]
        P1 = (state[2],state[3],state[4])
        P2 = (state[5],state[6],state[7])
        P3 = (state[8],state[9],state[10])
    #desno
        if   ((X < 5 and Y < 5) or (X > 4 and Y < 10)):
            Xnew = X
            Ynew = Y+1
            P1new = updateHori(P1)
            P2new = updateDigi(P2)
            P3new = updateVert(P3)
            if (Xnew !=P1new[0] or Ynew !=P1new[1] or Ynew!=P1new[1]+1\
                    or (Xnew != P2new[0] or Xnew != P2new[0] - 1 or Ynew != P2new[1] or Ynew != P2new[1] + 1)\
                    or (Ynew != P3new[1] or (Xnew != P3new[0] or Xnew != P3new[0]+1))):
                        Statenew = (Xnew, Ynew, P1new[0], P1new[1], P1new[2], P2new[0], P2new[1], P2new[2], P3new[0], P3new[1], P3new[2])
                        successors["Desno"] = Statenew

    #levo
        if  Y>0:
            Xnew = X
            Ynew = Y-1
            P1new = updateHori(P1)
            P2new = updateDigi(P2)
            P3new = updateVert(P3)
            if (Xnew !=P1new[0] and Ynew !=P1new[1] or Ynew!=P1new[1]+1\
                    or (Xnew != P2new[0] or Xnew != P2new[0] - 1 or Ynew != P2new[1] or Ynew != P2new[1] + 1)\
                    or (Ynew != P3new[1] or Xnew != P3new[0] or Xnew != P3new[0]+1)):
                        Statenew = (Xnew, Ynew, P1new[0], P1new[1], P1new[2], P2new[0], P2new[1], P2new[2], P3new[0], P3new[1], P3new[2])
                        successors["Levo"] = Statenew

        # gore
        if (X > 5 and Y > 5) or (X > 0 and Y < 6):
            Xnew = X-1
            Ynew = Y
            P1new = updateHori(P1)
            P2new = updateDigi(P2)
            P3new = updateVert(P3)
            if (Xnew !=P1new[0] or Ynew !=P1new[1] or Ynew!=P1new[1]+1\
                    or (Xnew != P2new[0] or Xnew != P2new[0] - 1 or Ynew != P2new[1] or Ynew != P2new[1] + 1)\
                    or (Ynew != P3new[1] or (Xnew != P3new[0] or Xnew != P3new[0]+1))):
                        Statenew = (Xnew, Ynew, P1new[0], P1new[1], P1new[2], P2new[0], P2new[1], P2new[2], P3new[0], P3new[1], P3new[2])
                        successors["Gore"] = Statenew
          #dole
        if (X<10):
            Xnew = X+1
            Ynew = Y
            P1new = updateHori(P1)
            P2new = updateDigi(P2)
            P3new = updateVert(P3)
            if (Xnew !=P1new[0] or (Ynew !=P1new[1] or Ynew!=P1new[1]+1)\
                    or (Xnew != P2new[0] or Xnew != P2new[0] - 1 or Ynew != P2new[1] or Ynew != P2new[1] + 1)\
                    or (Ynew != P3new[1] or Xnew != P3new[0] or Xnew != P3new[0]+1)):
                        Statenew = (Xnew, Ynew, P1new[0], P1new[1], P1new[2], P2new[0], P2new[1], P2new[2], P3new[0], P3new[1], P3new[2])
                        successors["Dolu"] = Statenew
        return successors

    def result(self , state , action):
        possible = self.successor(state)
        return possible[action]
    def actions(self, state):
        return self.successor(state).keys()

K = [int(KukaRedica),int(KukaKolona)]
IstrazhuvachInstance = Istrazhuvach((int(CoveceRedica),int(CoveceKolona),2,2,-1,2,8,-1,8,8,-1),K)
answer = astar_search(IstrazhuvachInstance)
print(answer.solution())
