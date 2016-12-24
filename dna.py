from utils import randomVector2
import random

class DNA():

    def __init__(self, game, genes=None):
        self.game = game
        if genes:
            self.genes = genes
        else:
            self.genes = []
            for i in range(self.game.lifespan):
                self.genes.append(randomVector2()*0.05)

    def crossover(self, partner):
        newgenes = []
        midpoint = int(random.random()*len(self.genes))
        newgenes += self.genes[:midpoint]
        newgenes += partner.genes[midpoint:]
        return DNA(self.game, newgenes)

    def mutation(self):
        for i in range(len(self.genes)):
            if random.random() < 0.005:
                self.genes[i] = randomVector2()*0.1