# Pathfinding Visualizer by Jeffery Xie
A visual pathfinding program that allows the user to create their own obstacles or mazes and then run different pathfinding algorithms on it. This program includes the ability to place weighted path nodes, the ability to generate a random maze using Prim's algorithm, a results display after each successful path found, and five different algorithms to choose from.

**Please make sure to read the first few lines of the "Extra Information" section! (Up until the algorithm explanations)**

# Table of Contents
* [Demo Images](#demo)
* [Features](#features)
* [Controls](#controls)
* [Requirements and Installation](#req)
* [Future Implementations](#future)
* [Extra Information](#extra)

# Demo Images <a name="demo"></a>
![search_demo](https://cdn.discordapp.com/attachments/770779709172613122/797213643833999400/demo.png)
![maze_demo](https://cdn.discordapp.com/attachments/770779709172613122/797213660619603998/maze.png)

# Features <a name="features"></a>
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
* The ability to pause and resume an algorithm that is in process to work through the problem with it.

# Controls <a name="controls"></a>
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
* Press the "p" key during any algorithm to pause/unpause it.
* Press the spacebar key to start the search after choosing a pathfinding algorithm.

# Requirements and Installation <a name="req"></a>
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
* You can start the program by running visualizer.py!

# Future Implementations <a name="future"></a>
* More maze generator algorithms (recursive division..?)
* Let the user search from a variety of different heuristics. (Diagonal distance..)
  * Will likely need to change my neighbourhood definition from a 4 neighbourhood adjacency to 8 adjacency
  * I've already implemented the euclidian distance heuristic, but realized that this is intended for problems where you are able to traverse the graph in any angle (not just up, down, right, left, diagonally). My program does not allow movement at any arbitrary angle like 23 degrees for example, so I am not using this heuristic.
* Implement more algorithms (bidirectional bfs, ida*, etc)

# Extra Information <a name="extra"></a>
Note that Pygame's graphics are going to be different depending on the machine / version of machine that you are using. I coded this on a windows machine so things look good for me, but on Mac for example text may be off center and things might look blurry or pixelated.

Also, keep in mind that since this program is taking time to draw every node that it creates and looks at, the algorithms will naturally run a little bit slower than usual, especially for the maze generating algorithm.
  * To make the algorithms run at normal speed, go to the files and remove the lines in the algorithm where it calls "draw()".
    * Ex. To speed up the maze generator algorithm, open prims.py, go to lines #95 and #190 and comment out the draw() calls.
