#!/usr/bin/env python
import numpy as np
import random
import benchmark_function

a = 0.72984
b_loc = 1.496172
b_glob = 1.496172

#TODO universal particle swarm. give a function and a search space

def random_vector(min, max, dimension):
    return np.array([random.uniform(min, max) for d in range(dimension)])


class Particle:

    def __init__(self, swarm):
        self.swarm = swarm
        self.velocity = np.array([0 for d in range(swarm.dimension)])
        self.location = random_vector(swarm.range_min, swarm.range_max, swarm.dimension)
        self.optimum = self.location
        self.optimum_val = swarm.function(self.optimum)

    def update(self,  global_optimum, global_optimum_val):
        global a, b_loc, b_glob
        #random vectors
        r_loc = random_vector(0, 1, self.swarm.dimension)
        r_glob = random_vector(0, 1, self.swarm.dimension)

        self.velocity = a * self.velocity + b_loc * r_loc * (self.optimum - self.location) + b_glob * r_glob * (global_optimum.optimum - self.location)

        self.location = self.location + self.velocity

        #update optima
        tmp = self.swarm.function(self.location)
        if self.optimum_val > tmp:
            self.optimum = self.location
            self.optimum_val = tmp

        if (self.optimum_val < global_optimum_val):
            return self
        else:
            return None

    def __str__(self):
        return "v = %s, l = %s, opt = %s, opt_val = %s" % (self.velocity, self.location, self.optimum, self.optimum_val)


class ParticleSwarm:

    def __init__(self, dimension, range_min, range_max, function, num_particles, max_iterations):
        self.dimension = dimension
        self.range_min = range_min
        self.range_max = range_max
        self.function = function
        self.max_iterations = max_iterations

        self.particles = [Particle(self) for e in range(num_particles)]

        self.global_optimum = self.particles[0].location
        self.global_optimum_val = self.particles[0].optimum_val

        # set global optimum
        for p in self.particles:
            if self.global_optimum_val > p.optimum_val:
                self.global_optimum = p
                self.global_optimum_val = p.optimum_val


    def optimize(self):
        for e in range(self.max_iterations):
            for p in self.particles:
                if p.update(self.global_optimum, self.global_optimum_val):
                    self.global_optimum = p
                    self.global_optimum_val = p.optimum_val



if __name__ == "__main__":
    p = ParticleSwarm(10, -100, 100, benchmark_function.sphere, 20, 200)
    p.optimize()
    print ("Optimum: {}".format(p.global_optimum))








#print ("OPTIMUM", global_optimum.optimum, " OPTIMUM VAL ", global_optimum.optimum_val)
