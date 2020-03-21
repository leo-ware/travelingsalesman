import matplotlib.pyplot as plt
import itertools
import random

# This is the class I will use to represent the map of the cities. When initialized,
# a new map is created.


class Network:
    def __init__(self, map_size=(15, 15), N=15):

        self.nodes = list(range(N))  # we use the first N integers to identify the nodes

        self.positions = dict.fromkeys(self.nodes)  # keeps track of their geographic positions
        for i in self.nodes:  # after they are randomly assigned
            self.positions[i] = (random.random() * map_size[0], random.random() * map_size[1])

        # keeps track of distances between nodes, calculates using their positions on the map
        # I wanted to use a dictionary for speed, but tuples are unhashable. So, I sort them and
        # put them in a string to use them as keys. This keeps lookups O(1)
        self.edges = {}
        for i, j in itertools.combinations(self.nodes, 2):
            dist = ((self.positions[i][0] - self.positions[j][0]) ** 2 + (
                        self.positions[i][1] - self.positions[j][1]) ** 2) ** 0.5
            self.edges[str(sorted((i, j)))] = dist  # sorted() so lookups will work

    # visualizes the cities using a matplotlibe scatter plot with the ticks removed
    def draw_map(self):
        plt.scatter([self.positions[i][0] for i in self.positions], [self.positions[i][1] for i in self.positions],
                    color='black')
        plt.title("Cities in Need of the Vaccine")
        plt.xticks([])
        plt.yticks([])
        plt.show()

    # This function takes in a network and a proposed route, and overlays a visualization of the
    # route on a visualization of the cities in the network

    def draw_route(self, route, text=""):
        # Plot the cities of the network
        plt.scatter([self.positions[i][0] for i in self.positions],
                    [self.positions[i][1] for i in self.positions], color='black')

        # plot the route with nice formatting
        plt.plot([self.positions[i][0] for i in route], [self.positions[i][1] for i in route], alpha=0.5,
                 linestyle='--', color='gray')
        plt.title("Planned Route through Cities"+text)

        # remove the ticks, this isn't a graph
        plt.xticks([])
        plt.yticks([])
        plt.show()

        # Also, print the score
        print('length =', self.traversal_time(route))

    # looks us the distance between two nodes using the edges dictionary
    # I used a function for this because of the while str(sorted()) part
    def distance(self, i, j):
        return self.edges[str(sorted((i, j)))]

    # just the sum of the distances in a route
    def traversal_time(self, route):
        time = 0
        for index, node in enumerate(route[:-1]):
            time += self.distance(node, route[index + 1])  # Trip is one way, return time doesn't matter
        return time
