# Pathfinding Visualizer by Jeffery Xie
A visual pathfinding program that allows the user to create their own obstacles or mazes and then run different pathfinding algorithms on it. This program includes the ability to place weighted path nodes, the ability to generate a random maze using Prim's algorithm, a results display after each successful path found, and five different algorithms to choose from.

**Please make sure to read the first few lines of the "Extra Information" section!**

# Table of Contents
* [Requirements and Installation](#req)
* [Features](#features)
* [Controls](#controls)
* [Future Implementations](#future)
* [Extra Information](#extra)

## Requirements and Installation <a name="req"></a>
Make sure you have a python version of 3.x or higher!

**Required Modules**
* To install, simply enter these commands into your terminal. (for macOS users, replace pip with pip3)
* For help with installing pip: visit https://pip.pypa.io/en/stable/installing/
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

## Features <a name="features"></a>
* Five Unique Pathfinding Algorithms
   * A* Search 
   * Dijkstras Algorithm 
   * Greedy Best First Search 
   * Breadth First Search 
   * Depth First Search 
* A built in maze generator algorithm (Prim's Algorithm)
* A real time visualization where you can see how each of the different pathfinding algorithms work.
* The ability to construct your own mazes / obstacles for the pathfinding algorithm.
  * Can also create weighted nodes for weighted algorithms!
* A results display that shows the following information after each successful completion (if a path was found).
  * The name of the algorithm.
  * The total cost of the solution (sum of all node weights from the path that was found).
  * The time in seconds taken to find the path.
  * The number of nodes that were visited / searched.
* A toggleable speed that you can change before / during the running of an algorithm.

## Controls <a name="controls"></a>
* Left click to place a node.
   * Your first click will be the start node. (Green)
   * Your second click will be the end node. (Red)
   * After start and end are defined, your next clicks will place walls or weights.
   * Press the "w" key along with left click to place a weighted node with cost = 9 (normal nodes cost 1).
   * Hold left click and move mouse to place multiple nodes at once.
* Left click on any algorithm to select it, and you can change the speed of the algorithm by clicking on the speed button.
  * Options available for speed: (Slow, Medium, Fast)
* Right click on a node to reset it.
   * Hold right click and move mouse to reset multiple nodes at once.
* Press the "c" key to reset the board.
* Press the "g" key to generate a random maze using Prim's algorithm.
* Press the spacebar key to start the search after choosing a pathfinding algorithm.

## Future Implementations <a name="future"></a>
* More maze generator algorithms (recursive division..?)
* Let the user search from a variety of different heuristics.
  * Will likely need to change my neighbourhood definition from a 4 neighbourhood adjacency to 8 adjacency
* Implement more algorithms (bidirectional bfs, ida*, swarm, etc)

## Extra Information <a name="extra"></a>
Note that Pygame's graphics are going to be different depending on the machine that you are using. On Mac for example, things might look more blurry / pixelated.

Also, keep in mind that since this program is taking time to draw every node that it creates / looks at, the algorithms will naturally run a little bit slower than usual, especially for the maze generating algorithm.
  * To make the algorithms run at normal speed, go to the files and remove the lines in the algorithm where it calls "draw()".
    * Ex. To speed up the maze generator algorithm, open prims.py, go to lines #72 and #163 and comment out the draw() calls.

**A Star Search**
* I've implemented a weighted A* search which can calculate shortest path in relation to cost when the path weights are not all the same. 
  * Note that not all A* searches are weighted!
* This implementation uses a priority queue for its frontier, which prioritizes nodes with the lowest F score.
  * F = G + H + node cost, where
    * G is the distance from current node to start node
    * and H is the estimated distance from current node to end node (calculated by heuristic)
* The runtime and space complexity depends on the heuristic.
  * The theoretical time and space complexity is O(b ^ d), where
    * b is the branching factor (number of successor nodes per state)
    * and d is the depth of the shortest path to the end node
  * I am using the Manhattan Distance which is an admissible heuristic. 
    * An admissible heuristic never overestimates the cost of reaching the goal node
* A* Search is guaranteed to return the shortest path.

**Greedy Best First Search**
* Greedy Best First Search is a weighted algorithm that does not guarantee the shortest path.
* It is similar to A* search, except it does not care about the G score.
  * This means that its evaluation for F score = H + node cost, where H is the heuristic. (Manhattan Distance)
* This implementation uses a priority queue for its frontier.
* The runtime and space complexity depends on the heuristic.
  * The worst case time and space complexity is O(b ^ m), where
    * b is the branching factor (number of successor nodes per state)
    * and m is the maximum depth of the search space

**Dijkstra's Algorithm**
* Dijkstra's Algorithm is a weighted algorithm that guarantees the shortest path.
* It is similar to A* search, except it does not use a heuristic.
  * This means that its evaluation for F score = G + node cost, where G is the distance from current node to start node
* This implementation uses a priority queue for its frontier.
* The time and space complexity is O(E log N), where 
  * E is the number of edges 
  * and N is number of nodes

**Breadth First Search**
* Breadth First Search is a non-weighted algorithm that guarantees the shortest path.
  * Note that this search treats every node as a cost = 1 node. This means that if there
  * are weighted nodes, it will treat them as normal nodes.
* Breadth First Search uses FIFO (queue).
* Time complexity is O(N + E), where N is number of nodes and E is number of edges
* Space complexity is O(N) where N is the number of nodes in the call stack

**Depth First Search**
* Depth First Search is a non-weighted algorithm that does not guarantee the shortest path.
* Depth First Search uses LIFO (stack).
  * The order of traversal for DFS is up, right, down, left
* Time complexity is O(N + E), where N is number of nodes and E is number of edges
* Space complexity is O(N), where N is the number of nodes in the call stack
