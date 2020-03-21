# this file runs the program, some comments on how to change the parameters are shown below


from network import Network
from greedy import Greedy
from annealing import Annealing

# A call to initialize an instance of the network class

# will create a new map with new cities
# change the N parameter to adjust how many cities appear, annealer does better with fewer

n = Network(N=15)

# Calls the greedy and annealer algorithms on the network created in the above block.
# Visualizes results for comparison.

print("Greedy")

g = Greedy(n)
g.run()
n.draw_route(g.route, text=" - Greedy")

print()
print("Annealing")

a = Annealing(n, T=50, c=0.9995)  # larger T means more time exploring and less time descending
# If you make T much bigger, add more nines to c so you
# don't get a zero division error

a.run(n_times=12000)  # can be slow
n.draw_route(a.route, text=" - Annealing")
a.score_plot()
a.T_plot()
