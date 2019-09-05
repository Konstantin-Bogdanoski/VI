# Python modul vo koj se implementirani algoritmite za informirano prebaruvanje

# ______________________________________________________________________________________________
# Improtiranje na dopolnitelno potrebni paketi za funkcioniranje na kodovite

import sys
import bisect

infinity = float('inf')  # sistemski definirana vrednost za beskonecnost


# ______________________________________________________________________________________________
# Definiranje na pomosni strukturi za cuvanje na listata na generirani, no neprovereni jazli

class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): A Last In First Out Queue.
        FIFOQueue(): A First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    Note that isinstance(Stack(), Queue) is false, because we implement stacks
    as lists.  If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)


def Stack():
    """A Last-In-First-Out Queue."""
    return []


class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""

    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A) / 2:
            self.A = self.A[self.start:]
            self.start = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.start:]


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    Also supports dict-like lookup. This structure will be most useful in informed searches"""

    def __init__(self, order=min, f=lambda x: x):
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        return len(self.A)

    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.A)

    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)


# ______________________________________________________________________________________________
# Definiranje na klasa za strukturata na problemot koj ke go resavame so prebaruvanje
# Klasata Problem e apstraktna klasa od koja pravime nasleduvanje za definiranje na osnovnite karakteristiki
# na sekoj eden problem sto sakame da go resime


class Problem:
    """The abstract class for a formal problem.  You should subclass this and
    implement the method successor, and possibly __init__, goal_test, and
    path_cost. Then you will create instances of your subclass and solve them
    with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """Given a state, return a dictionary of {action : state} pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once. Iterators will work fine within the framework. Yielding is not supported in Python 2.7"""
        raise NotImplementedError

    def actions(self, state):
        """Given a state, return a list of all actions possible from that state"""
        raise NotImplementedError

    def result(self, state, action):
        """Given a state and action, return the resulting state"""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Implement this
        method if checking against a single self.goal is not enough."""
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________
# Definiranje na klasa za strukturata na jazel od prebaruvanje
# Klasata Node ne se nasleduva

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        "List the nodes reachable in one step from this node."
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        "Return a child node from this node"
        next = problem.result(self.state, action)
        return Node(next, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next))

    def solution(self):
        "Return the sequence of actions to go from the root to this node."
        return [node.action for node in self.path()[1:]]

    def solve(self):
        "Return the sequence of states to go from the root to this node."
        return [node.state for node in self.path()[0:]]

    def path(self):
        "Return a list of nodes forming the path from the root to this node."
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        return list(reversed(result))

    # We want for a queue of nodes in breadth_first_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)



# ________________________________________________________________________________________________________
#Pomosna funkcija za informirani prebaruvanja
#So pomos na ovaa funkcija gi keshirame rezultatite od funkcijata na evaluacija

def memoize(fn, slot=None):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, store results in a dictionary."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memoized_fn(*args):
            if not memoized_fn.cache.has_key(args):
                memoized_fn.cache[args] = fn(*args)
            return memoized_fn.cache[args]

        memoized_fn.cache = {}
    return memoized_fn


# ________________________________________________________________________________________________________
#Informirano prebaruvanje vo ramki na graf

def best_first_graph_search(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""

    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return None


def greedy_best_first_graph_search(problem, h=None):
    "Greedy best-first search is accomplished by specifying f(n) = h(n)"
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)


def astar_search(problem, h=None):
    "A* search is best-first graph search with f(n) = g(n)+h(n)."
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


# ________________________________________________________________________________________________________
#Dopolnitelni prebaruvanja
#Recursive_best_first_search e implementiran
#Kako zadaca za studentite da gi implementiraat SMA* i IDA*

def recursive_best_first_search(problem, h=None):
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.goal_test(node.state):
            return node, 0  # (The second value is immaterial)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, infinity
        for s in successors:
            s.f = max(s.path_cost + h(s), node.f)
        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = infinity
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f

    node = Node(problem.initial)
    node.f = h(node)
    result, bestf = RBFS(problem, node, infinity)
    return result



# _________________________________________________________________________________________________________
#PRIMER 2 : PROBLEM NA SLOZUVALKA
#OPIS: Dadena e slozuvalka 3x3 na koja ima polinja so brojki od 1 do 8 i edno prazno pole
# Praznoto pole e obelezano so *. Eden primer na slozuvalka e daden vo prodolzenie:
#  -------------
#  | * | 3 | 2 |
#  |---|---|---|
#  | 4 | 1 | 5 |
#  |---|---|---|
#  | 6 | 7 | 8 |
#  -------------
#Problemot e kako da se stigne do nekoja pocetna raspredelba na polinjata do nekoja posakuvana, na primer do:
#  -------------
#  | * | 1 | 2 |
#  |---|---|---|
#  | 3 | 4 | 5 |
#  |---|---|---|
#  | 6 | 7 | 8 |
#  -------------
#AKCII: Akciite ke gi gledame kako dvizenje na praznoto pole, pa mozni akcii se : gore, dole, levo i desno.
#Pri definiranjeto na akciite mora da se vnimava dali akciite voopsto mozat da se prevzemat vo dadenata slozuvalka
#STATE: Sostojbata ke ja definirame kako string koj ke ima 9 karakteri (po eden za sekoe brojce plus za *)
#pri sto stringot ke se popolnuva so izminuvanje na slozuvalkata od prviot kon tretiot red, od levo kon desno.
# Na primer sostojbata za pocetnata slozuvalka e: '*32415678'
# Sostojbata za finalnata slozuvalka e: '*12345678'
# ________________________________________________________________________________________________________
#

default_goal = '*12345678' #predefinirana cel

#Ke definirame 3 klasi za problemot
#Prvata klasa nema implementirano nikakva hevristika

class P8(Problem):

    name = 'No Heuristic'

    def __init__(self, goal=default_goal, initial=None, N=20):
        self.goal = goal
        self.initial = initial

    def successor(self, state):
        return successor8(state)

    def actions(self, state):
        return self.successor(state).keys()

    def h(self, node):
        """Heuristic for 8 puzzle: returns 0"""
        return 0

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

#Slednite klasi ke nasleduvaat od prethodnata bez hevristika so toa sto ovde ke ja definirame i hevristikata

class P8_h1(P8):
    """ Slozuvalka so hevristika
    HEVRISTIKA: Brojot na polinja koi ne se na vistinskoto mesto"""

    name = 'Out of Place Heuristic'

    def h(self, node):
        """Funkcija koja ja presmetuva hevristikata,
        t.e. razlikata pomegu nekoj tekoven jazel od prebaruvanjeto i celniot jazel"""
        matches = 0
        for (t1, t2) in zip(node.state, self.goal):
            #zip funkcijata od dve listi na vlez pravi edna lista od parovi (torki)
            #primer: zip(['a','b','c'],[1,2,3]) == [('a',1),('b',2),('c',3)]
            # zip('abc','123') == [('a','1'),('b','2'),('c','3')]
            if t1 != t2:
                matches = + 1
        return matches


class P8_h2(P8):
    """ Slozuvalka so hevristika
    HEVRISTIKA: Menheten rastojanie do celna sostojba"""

    name = 'Manhattan Distance Heuristic (MHD)'

    def h(self, node):
        """Funkcija koja ja presmetuva hevristikata,
        t.e. Menheten rastojanieto pomegu nekoj tekoven jazel od prebaruvanjeto i celniot jazel, pri sto
        Menheten rastojanieto megu jazlite e zbir od Menheten rastojanijata pomegu istite broevi vo dvata jazli"""
        sum = 0
        for c in '12345678':
            sum = + mhd(node.state.index(c), self.goal.index(c)) #pomosna funkcija definirana vo prodolzenie
        return sum


# Za da mozeme da go definirame rastojanieto treba da definirame koordinaten sistem
# Pozetokot na koordinatniot sistem e postaven vo gorniot lev agol na slozuvalkata
# Definirame recnik za koordinatite na sekoe pole od slozuvalkata
coordinates = {0: (0, 0), 1: (1, 0), 2: (2, 0),
               3: (0, 1), 4: (1, 1), 5: (2, 1),
               6: (0, 2), 7: (1, 2), 8: (2, 2)}

#Funkcija koja presmetuva Menheten rastojanie za slozuvalkata
#Na vlez dobiva dva celi broja koi odgovaraat na dve polinja na koi se naogaat broevite za koi treba da presmetame rastojanie
def mhd(n, m):
    x1, y1 = coordinates[n]
    x2, y2 = coordinates[m]
    return abs(x1 - x2) + abs(y1 - y2)



def successor8(S):
    """Pomosna funkcija koja generira recnik za sledbenicite na daden jazel"""

    blank = S.index('*') #kade se naoga praznoto pole

    succs = {}

    # GORE: Ako praznoto pole ne e vo prviot red, togas vo sostojbata napravi swap
    # na praznoto pole so brojceto koe se naoga na poleto nad nego
    if blank > 2:
        swap = blank - 3
        succs['GORE'] = S[0:swap] + '*' + S[swap + 1:blank] + S[swap] + S[blank + 1:]

    # DOLE: Ako praznoto pole ne e vo posledniot red, togas vo sostojbata napravi swap
    # na praznoto pole so brojceto koe se naoga na poleto pod nego
    if blank < 6:
        swap = blank + 3
        succs['DOLE'] = S[0:blank] + S[swap] + S[blank + 1:swap] + '*' + S[swap + 1:]

    # LEVO: Ako praznoto pole ne e vo prvata kolona, togas vo sostojbata napravi swap
    # na praznoto pole so brojceto koe se naoga na poleto levo od nego
    if blank % 3 > 0:
        swap = blank - 1
        succs['LEVO'] = S[0:swap] + '*' + S[swap] + S[blank + 1:]

    # DESNO: Ako praznoto pole ne e vo poslednata kolona, togas vo sostojbata napravi swap
    # na praznoto pole so brojceto koe se naoga na poleto desno od nego
    if blank % 3 < 2:
        swap = blank + 1
        succs['DESNO'] = S[0:blank] + S[swap] + '*' + S[swap + 1:]

    return succs

# So vaka definiraniot problem mozeme da gi koristime site informirani, no i neinformirani prebaruvanja
# Vo prodolzenie se dadeni mozni povici (vnimavajte za da moze da napravite povik mora da definirate problem)
#
#    s='*32415678'
#    p1=P8(initial=s)
#    p2=P8_h1(initial=s)
#    p3=P8_h2(initial=s)
#
#    answer1 = greedy_best_first_graph_search(p1)
#    print answer1.solve()
#
#    answer2 = greedy_best_first_graph_search(p2)
#    print answer2.solve()
#
#    answer3 = greedy_best_first_graph_search(p3)
#    print answer3.solve()
#
#    answer4 = astar_search(p1)
#    print answer4.solve()
#
#    answer5 = astar_search(p2)
#    print answer5.solve()
#
#    answer6 = astar_search(p3)
#    print answer6.solve()
#
#    answer7 = recursive_best_first_search(p1)
#    print answer7.solve()
#
#    answer8 = recursive_best_first_search(p2)
#    print answer8.solve()
#
#    answer9 = recursive_best_first_search(p3)
#    print answer9.solve()


######################################################################################
#MOLEKULA INFORMIRANO
######################################################################################
def h(self, node):
	S = node.state
	return abs(S[0] –S[2]) + abs(S[1] –S[3]) + \
		abs(S[2] –S[4]) + abs(S[3] –S[5]) + \
		abs(S[0] –S[4]) + abs(S[1] –S[5])

######################################################################################
######################################################################################
######################################################################################
#LAB_02_PreprekiInfor
######################################################################################
######################################################################################
######################################################################################

#Vcituvanje na vleznite argumenti za test primerite

CoveceRedica = input()
CoveceKolona = input()
KukaRedica = input()
KukaKolona = input()

#Vasiot kod pisuvajte go pod ovoj komentar

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
######################################################################################
######################################################################################
######################################################################################





######################################################################################
######################################################################################
######################################################################################
#LAB_02_Misioneri
######################################################################################
######################################################################################
######################################################################################
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
#######################################################################################
#######################################################################################
#######################################################################################






#######################################################################################
#######################################################################################
#######################################################################################
#FARMER_AUDITORISKI
#######################################################################################
#######################################################################################
#######################################################################################
# Функција за проверка на легалност на произволна состојба
def legalna(state):
	farmer = state[0]
	volk = state[1]
	jare = state[2]
	zelka = state[3] 
	if(volk == jare and farmer != volk):
		return False
	elif(jare == zelka and farmer != jare):
		return False
	return True

class Farmer(Problem):
	def __init__(self, initial, goal):
		self.initial = initial
		self.goal = goal
	def goal_test(self, state):
	"""Враќа True ако состојбата state е целна состојба."""
		farmer = state[0]
		volk = state[1]
		jare = state[2]
		zelka = state[3]
		return (farmer == self.goal[0]) and (volk== self.goal[1]) \
			and(jare== self.goal[2]) and(zelka== self.goal[3]) 
	def successor(self, state):
	"""Враќа речник од следбеници на состојбата"""
		successors = dict()
		farmer, volk = state[0], state[1]  
		jare, zelka = state[2], state[3]

		# Фармерот се пренесува самиот себеси
		if (farmer == 'w'):
			farmerNew= 'e'
		else:
			farmerNew = 'w'
		Statenew = (farmerNew, volk, jare, zelka)
		if (legalna(Statenew)):
			successors['Farmer_nosi_farmer'] = Statenew

		# Фармерот го пренесува волкот
		if (farmer == volk):
			if (farmer == 'w'):
				volkNew = 'e'
			else:
				volkNew = 'w'
			Statenew = (farmerNew, volkNew, jare, zelka)
			if (legalna(Statenew)):
				successors['Farmer_nosi_volk'] = Statenew
		#Аналогно се дефинира и ‘Farmer_nosi_jare’и ‘Farmer_nosi_zelka’

		return successors

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		possible = self.successor(state)
		return possible[action]

	def h(self, node):
		S = node.state
		vrednost = 0
		for i in range(0, len(S)):
			if(S[i] != self.goal[i]):
				vrednost = vrednost+ 1
		return vrednost


FarmerInstance= Farmer(('e','e','e','e'), ('w','w','w','w'))
answer = astar_search(FarmerInstance)
print answer.solve()
#######################################################################################
#######################################################################################
#######################################################################################






#######################################################################################
#######################################################################################
#######################################################################################
#SLOZHUVALKA_AUDITORISKI
#######################################################################################
#######################################################################################
#######################################################################################
class P8(Problem):
	name = 'No Heuristic'
	def __init__(self, goal='*12345678', initial=None):
		self.goal = goal
		self.initial = initial
	def successor(self, state):
		return successor8(state)
	def actions(self, state):
		return self.successor(state).keys()
	def h(self, node):
	""" Евристика за сложувалката со 8 полиња: враќа 0"""
		return 0
	def result(self, state, action):
		possible = self.successor(state)
		return possible[action]

class P8_h1(P8):
	""" Сложувалка со евристика
	ЕВРИСТИКА: 
		Број на полиња кои не се на вистинското место."""
	name = 'Out of Place Heuristic'
	defh(self, node):
	"""Функција која ја пресметува евристиката, т.е. разликата помеѓу некој тековен јазел од пребарувањето и целниот јазел"""
	matches = 0
	for(t1, t2) in zip(node.state, self.goal):
		#zip функцијата од две листи на влез прави една листа од парови 		(торки)
		#пример: zip(['a','b','c'],[1,2,3]) == [('a',1),('b',2),('c',3)]
		# zip('abc','123') == [('a','1'),('b','2'),('c','3')]
		if t1 != t2:
		matches += 1
	return matches

class P8_h2(P8):
	""" Сложувалка со евристика
	ЕВРИСТИКА: 
		Менхетн растојание до целната состојба."""
	name = 'Manhattan Distance Heuristic (MHD)'
	defh(self, node):
	"""Функција која ја пресметува евристиката, т.e. Менхетн растојанието помеѓу некој тековен јазел од пребарувањето и целниот јазел, при што Менхетн растојанието помеѓу јазлите е збир од Менхетн растојанијата помеѓу истите броеви во двата јазли."""
	sum = 0
	for c in '12345678':
		sum = + mhd(node.state.index(c), self.goal.index(c))
	#помошна функција дефинирана во продолжение
	return sum

coordinates = {0: (0, 0), 1: (1, 0), 2: (2, 0),3: (0, 1), 4: (1, 1), 5: (2, 1),6: (0, 2), 7: (1, 2), 8: (2, 2)}

def mhd(n, m):
	x1, y1 = coordinates[n]
	x2, y2 = coordinates[m]
	return abs(x1 -x2) + abs(y1 -y2)

def successor8(S):
	"""Помошна функција која генерира речник за следбениците на даден јазел"""
	blank = S.index('*') 
	#kade se naoga praznoto pole 
	succs= {}
	# ГОРЕ: Ако празното поле не е во првиот ред, тогаш во состојбата  направиswapна празното поле со бројчето кое се наоѓа на полето над него
	if blank > 2:
		swap = blank - 3
		succs['GORE'] = S[0:swap] + '*'+ S[swap + 1:blank] + S[swap] + S[blank + 1:]
	# ДОЛУ: Ако празното поле не е во последниот ред, тогаш во состојбата направи swap на празното поле со бројчето кое се наоѓа на полето под него
	if blank < 6:
		swap = blank + 3
		succs['DOLU'] = S[0:blank] + S[swap] + S[blank + 1:swap] + '*'+ S[swap + 1:]

	# ЛЕВО: Ако празното поле не е во првата колона, тогаш во состојбата направиswapна празното поле со бројчето кое се наоѓа на полето лево од него
	if blank % 3 > 0:
		swap = blank - 1
		succs['LEVO'] = S[0:swap] + '*' + S[swap] + S[blank + 1:]
	# ДЕСНО: Ако празното поле не е во последната колона, тогаш во состојбата направиswapна празното поле со бројчето кое се наоѓа на полето десно од него
	if blank % 3 < 2:
		swap = blank + 1
		succs['DESNO'] = S[0:blank] + S[swap] + '*'+ S[swap + 1:]
	return succs

s = '*32415678'
p1 = P8(initial = s)
p2 = P8_h1(initial = s)
p3 = P8_h2(initial = s) 
answer1 = greedy_best_first_graph_search(p1)
printanswer1.solve()

