from math import e
import random
import matplotlib.pyplot as plt

# Annealing is complicated and takes a lot more code than greedy, mostly
# because there are a lot of variables to keep track of, but also because
# of all the visualization equipment


class Annealing:
    def __init__(self, network, T=100, c=0.9):

        # same as in greedy, set the network for the class, start the route at 0
        self.network = network
        self.route = [0] + [i for i in self.network.nodes if i != 0]

        # the temperature and cooling parameters. These control how often
        # worse solutions are accepted in place of better ones
        self.T = T
        self.c = c

        # keeps track of our best score so far
        self.score = float('inf')  # we are minimizing => initialize at infinity

        # keep track of the progess of the model, useful for visualization
        self.score_history = [self.score]
        self.route_history = [self.route]
        self.T_history = [self.T]

    def accept(self, old_score, new_score):

        # if it's better, take it
        if new_score < old_score:
            return True
        else:

            # This computational nightmare is the python implementation of the
            # acceptance function. Because of rounding and machine limits, we need
            # to be very careful when dealing with very big or very small numbers

            q = (new_score - old_score) / self.T
            t = 1
            for _ in range(round(q - 1)):
                t *= (1 / e)
                if t == 0.0:
                    break
            t *= 1 / (e ** (q - round(q - 1)))
            return t > random.random()

    # picks two random list elements and switches them, avoiding moving 0
    def swap2op(self):
        new = [i for i in self.route]
        length = len(new) - 1
        i, j = random.randint(1, length), random.randint(1, length)  # starting city cannot be changed
        new[i], new[j] = new[j], new[i]
        return new

    # puts the other functions together, swapping, checking, and accepting
    def run(self, n_times=1000):
        for _ in range(n_times):

            # create the new route and check the score
            new_route = self.swap2op()
            new_score = self.network.traversal_time(new_route)

            # decide whether to accept it
            if self.accept(self.score, new_score):
                self.route = new_route
                self.score = new_score

            # cool the temperature geometrically
            self.T *= self.c

            # remember the current state for later visualization
            self.score_history.append(self.score)
            self.route_history.append(self.route)
            self.T_history.append(self.T)

    # just plots the history of the score
    def score_plot(self):

        plt.plot(self.score_history)
        plt.title("Score over Iterations - Annealing")
        plt.xlabel("Iterations (log)")
        plt.ylabel("Score")
        plt.show()

    # just plots the history of the temperature, mostly for
    # comparison with the score plot above
    def T_plot(self):
        plt.plot(self.T_history, label="T")
        plt.title("Temperature (T) over Iterations - Annealing")
        plt.xlabel("Iterations (log)")
        plt.ylabel("T")
        plt.show()
