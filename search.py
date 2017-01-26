# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def startingState(self):
    """
    Returns the start state for the search problem
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
    """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
    util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """

  stack = util.Stack()  #Lifo Queue
  start = problem.startingState()   #root node
  visited = set()   #set of unique visited coords
  path = []
  print("Start: " + str(start))
  stack.push((start, 'None'))
  # ALSO NEED TO KEEP TRACK OF EACH PARENT OF THE POPPED NODE SO WE CAN TRACE BACK THE PATH!!!!!!
  if problem.isGoal(start):
    return start

  # Main loop --> nodes that haven't been visited
  while not stack.isEmpty():
    curr_node = stack.pop() # pop queue
    adjacent = problem.successorStates(curr_node)    # get successor states of curr_node
    # print("Current node: " + str(curr_node))
    # print("Adjacent: " + str(adjacent)) # in form of coord, dir, cost
    # print("Adjacent coords:" + str(adjacent[1][0])) #[i][0] is coordinate
    # print("Visited coords: " + str(visited))
    if problem.isGoal(curr_node):
        print("Found solution")
        path.append(curr_node)
        return path

    if curr_node not in visited:
        visited.add(curr_node)  # add curr_node to visited
        path.append(curr_node)


        for adj in adjacent:
            # print("Nodes adj to curr: "+ str(adj))
            # print(adj[0])
            stack.push(adj[0])
    pass
  util.raiseNotDefined()


def breadthFirstSearch(problem):
  # "Search the shallowest nodes in the search tree first. [p 81]"
  Q = util.Queue() #Fifo queue
  start = problem.startingState()
  visited = set()
  path = []
  print("Start: " + str(start))
  Q.push(start)

  if problem.isGoal(start):
    return start

  while not Q.isEmpty():
    curr_node = Q.pop()
    adjacent = problem.successorStates(curr_node)

    if problem.isGoal(curr_node):
        print("Found solution")
        path.append(curr_node)
        return path

    if curr_node not in visited:
      visited.add(curr_node)
      path.append(curr_node)

      for adj in adjacent:
        print("Coords adj to curr: "+ str(adj))
        Q.push(adj[0])

  pass
  util.raiseNotDefined()

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
