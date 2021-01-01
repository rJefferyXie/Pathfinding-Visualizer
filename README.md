# Pathfinding Visualizer by Jeffery Xie
A visual pathfinding program that allows the user to create their own obstacles or mazes and then run different pathfinding algorithms on it. This program includes the ability to place weighted path nodes, a results display after each successful path found, and five different algorithms to choose from.

# Requirements and Installation
**Required Modules**
* To install, simply enter these commands into your terminal. (for macOS users, replace pip with pip3)
* pip install pygame
  * If the command above does not work, visit https://www.pygame.org/wiki/GettingStarted for help.

**Setting up Repository**
* To clone repository, press the green "Code" button, and copy the HTTPS to your clipboard.
* Create a new project in your code editor or IDE of choice.
* Import the HTTPS url into version control on your new project.
* Two Examples:
  * If using pycharm, go to VCS --> get from version control --> paste the url --> clone
  * If using Visual Studio Code, go to explorer (ctrl + shift + e) --> clone repository --> paste the url --> clone

**Running**
* You can run the program by running visualizer.py!

# Controls
Left click to place a node.
   * Your first click will be the start node. (Green)
   * Your second click will be the end node. (Red)
   * After start and end are defined, your next clicks will place walls or weights.
   * Press the "w" key along with left click to place a weighted node with cost = 9 (normal nodes cost 1).
   * Hold left click and move mouse to place multiple nodes at once.
  
Left click on any algorithm to select it, and you can toggle the speed of the algorithm by clicking on the speed button.
  * Options available for speed: (Slow, Medium, Fast)
   
Right click on a node to reset it.
   * Hold right click and move mouse to reset multiple nodes at once.

Press the "c" key to reset the board.

Press the spacebar key to start the search after choosing a pathfinding algorithm.

# Features
Five Unique Pathfinding Algorithms
   * A* Search 
   * Dijkstras Algorithm 
   * Greedy Best First Search 
   * Breadth First Search 
   * Depth First Search 

A real time visualization where you can see how each of the different pathfinding algorithms work.

The ability to construct your own mazes / obstacles for the pathfinding algorithm.
  * Can also create weighted nodes for weighted algorithms!

A results display that shows the following information after each successful completion (only updates if a path was found).
  * The name of the algorithm.
  * The total cost of the solution (sum of all node weights from the path that was found).
  * The time in seconds taken to find the path.
  * The number of nodes that were visited / searched.

A toggleable speed that you can change before / during the running of an algorithm.

# Extra Information
**A Star Search**
* I've implemented a weighted A* search which can calculate shortest path in relation to cost when the path weights are not all the same. 
  * Note that not all A* searches are weighted!
* This implementation uses a priority queue for its frontier, which prioritizes nodes with the lowest F score.
  * F = G + H, where
    * G is the distance from current node to start node
    * and H is the estimated distance from current node to end node (calculated by heuristic)
* The runtime and space complexity depends on the heuristic.
  * The theoretical time and space complexity is O(b ^ d), where
    * b is the branching factor (number of successor nodes per state)
    * and d is the depth of the shortest path to the end node
  * I am using the Manhattan Distance which is an admissible heuristic. 
    * An admissible heuristic never overestimates the cost of reaching the goal node
* A* Search is guaranteed to return the shortest path.


# Future Implementations
A maze generator (recursive divison..?)

Let the user search from a variety of different heuristics.
  * Will likely need to change my neighbourhood definition from a 4 neighbourhood adjacency to 8 adjacency

Implement more algorithms (bidirectional bfs, ida*, swarm, etc)
