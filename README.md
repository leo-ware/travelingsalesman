# travelingsalesman
A couple optimization algorithms for the traveling salesman. The best way to explore the program is through 
the run.ipynb file.

The network class creates a random network of cities on a 2d plane, and the greedy and annealing algorithms 
try to find the fastest way to traverse it. The visualize class draws the routes each of them found, and 
shows the progress of the annealing algorithm as it iterates.

The greedy algorithm, starting from the point set by the network, looks through all the other points and finds
the closest one and then moves there. The annealing algorithm starts with a random path and tries to
improve it by swapping the positions of two cities in the order it has planned.

The annealing algorithm uses an exponential acceptance function and geometrically decreasing temperature. 
You can control the initial temperature and rate of decline when initializing the run. There is some help text
in the run file.

Note that, in the run, you have to close each chart before the next one gets displayed.
