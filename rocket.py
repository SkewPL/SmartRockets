from dna import DNA
from pygame import *
from pygame.math import *

class Rocket(object):

    def __init__(self, game, dna=None):
        self.game = game
        size = self.game.screen.get_size()
        self.pos = Vector2(size[0]/2, size[1] - 100)
        self.vel = Vector2(0,0)
        self.acc = Vector2()
        self.dna = dna if dna else DNA(self.game)
        self.fitness = 0.0
        self.crushed = False
        self.completed = False
        self.completed_in = 0

    def applyForce(self, force):
        self.acc += force

    def update(self):
        if not self.crushed and not self.completed:
            # Apply force from DNA
            self.applyForce(self.dna.genes[self.game.lifecount])

            # Update velocity and position
            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0

            # Check if target is achieved
            if self.game.environment.check_target(self.pos):
                self.completed = True
                self.game.population.living -= 1
                self.completed_in = self.game.population.generation
                if self.game.population.target_achieved == 0:
                    self.game.population.target_achieved = self.game.population.generation

            # Check if we hit the wall
            if self.game.environment.check_walls(self.pos):
                self.crushed = True
                self.game.population.living -= 1

            # Check if we hit the obstruction
            if self.game.environment.check_obstructions(self.pos):
                self.crushed = True
                self.game.population.living -= 1

    def calcFitness(self):
        dist = self.pos.distance_to(Vector2(self.game.environment.target))
        self.fitness = 1.0 / dist

        if self.completed:
            self.fitness *= 1 + (self.completed_in/self.game.lifespan)
        elif self.crushed:
            self.fitness *= 0.1

    def draw(self):
        # Create surface and fill it with white color
        s = Surface((5,20),SRCALPHA)
        if self.completed: s.fill((255, 0, 100, 200))
        else: s.fill((255, 255, 255, 200))

        # Rotate it
        angle = self.vel.angle_to(Vector2(1,0))
        s = transform.rotate(s, angle+90)

        # Blit onto screen
        size = s.get_size()
        self.game.screen.blit(s, (self.pos.x-(size[0]/2), self.pos.y-(size[1]/2)))