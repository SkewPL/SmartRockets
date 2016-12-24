from rocket import Rocket
import random

class Population():

    def __init__(self, game):
        self.game = game
        self.generation = 0
        self.target_achieved = 0
        self.maxfit = 0
        self.living = self.game.rockets
        self.rockets = []
        self.matingpool = []

        for i in range(self.game.rockets):
            self.rockets.append(Rocket(self.game))

    def update(self):
        for rocket in self.rockets:
            rocket.update()

        self.game.lifecount += 1
        if self.living == 0 or self.game.lifecount == self.game.lifespan:
            self.evaluate()
            self.selection()
            self.game.lifecount = 0

    def evaluate(self):
        # Calculate fitness of all rockets, and find out max fitness
        self.maxfit = 0
        for rocket in self.rockets:
            rocket.calcFitness()
            if rocket.fitness > self.maxfit:
                self.maxfit = rocket.fitness

        # Normalize fitness in all rockets
        for rocket in self.rockets:
            rocket.fitness /= self.maxfit

        # Add rockets to mating pool based on their fitness
        self.matingpool = []
        for i, rocket in enumerate(self.rockets):
            n = int(rocket.fitness * 100)
            self.matingpool += [i]*n

    def selection(self):
        newrockets = []
        for i in range(len(self.rockets)):
            parentA = self.rockets[random.choice(self.matingpool)].dna
            parentB = self.rockets[random.choice(self.matingpool)].dna
            childDNA = parentA.crossover(parentB)
            childDNA.mutation()
            newrockets.append(Rocket(self.game, childDNA))
        self.generation += 1
        self.rockets = newrockets
        self.living = len(self.rockets)
        self.matingpool = []

    def draw(self):
        for rocket in self.rockets:
            rocket.draw()