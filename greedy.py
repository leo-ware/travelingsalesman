# A greedy algorithm to solve the problem. Notice how little code this requires. In terms of
# developer time, greedy is probably the best algorithm.


class Greedy:
    def __init__(self, network):
        self.network = network
        self.route = []

    def run(self):

        # gets the names of the nodes and makes sure 0 is the first node
        # THis is because in the problem, we wouldn't be able to start anywhere in the problem
        not_visited = [i for i in self.network.nodes]
        not_visited.remove(0)
        route = [0]

        # iterates though unvisited nodes, finds the closest, and adds it to the route
        while not_visited:
            best = [None, float('inf')]
            for node in not_visited:
                dist = self.network.distance(route[-1], node)
                if dist < best[1]:  # is this one closer than the current winner?
                    best = [node, dist]
            route.append(best[0])  # add the best node to the route
            not_visited.remove(best[0])

        # send the route local variable to the class
        self.route = route
