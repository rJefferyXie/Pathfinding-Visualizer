# Pathfinding Visualizer by Jeffery Xie

You can run the program by running visualizer.py!

**Controls**
* Left click to place a node.
    * Your first click will be the start node. (Green)
    * Your second click will be the end node. (Red)
    * After start and end are defined, your next clicks will place walls or weights.
    * Press the "w" key along with left click to place a weighted node with cost = 9 (normal nodes cost 1).
* Right click on a node to reset it.
* Press the "c" key to reset the board.
* Left click on any algorithm to select it, and you can toggle the speed of the algorithm by clicking on the speed button.
    * Options available for speed: (Slow, Medium, Fast)
* Press the spacebar key to run the algorithm after choosing a pathfinding algorithm.

**Features**
* A results display that shows the following information after each successful completion (only updates if a path was found).
    * The name of the algorithm.
    * The total cost of the solution (sum of all node weights from the path that was found).
    * The time in seconds taken to find the path.
    * The number of nodes that were visited / searched.
* Five Unique Pathfinding Algorithms
    * A* Search
        * Very Good
    * Dijkstras Algorithm
        * Decent
    * Greedy Best First Search
        * Good
    * Breadth First Search
        * Good
    * Depth First Search
        * Generally Very Bad
* The ability to construct your own mazes / obstacles for the pathfinding algorithm.
    * Can also create weighted nodes for weighted algorithms!
* A toggleable speed that you can change before / during the running of an algorithm.
* A real time visualization where you can see how each of the different pathfinding algorithms work.

**Future Implementations**
* Let the user search from a variety of different heuristics.
* Implement more algorithms (bidirectional bfs, ida*, swarm, etc)
