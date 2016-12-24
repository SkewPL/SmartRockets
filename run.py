import pygame
from time import time, sleep

from environment import Environment
from population import Population
from debug import Debug

class Game(object):

    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))

        # Global variables
        self.max_tps = 0
        self.max_fps = 30
        self.lifespan = 10000
        self.rockets = 100

        self.lifecount = 0
        self.environment = Environment(self)
        self.population = Population(self)
        self.debug = Debug(self)

        # Local variables
        self.running = True
        self.simulating = False

        self.tps_counter = 0
        self.tps_timer = 0
        self.tps_value = 0

        self.fps_counter = 0
        self.fps_timer = 0
        self.fps_value = 0

        self.sec_timer = 0

        # Main loop
        while self.running:
            # Get events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.simulating:
                        self.simulating = True
                    elif event.key == pygame.K_d:
                        self.environment.obstructions = []
                    elif event.key == pygame.K_t:
                        self.environment.target = pygame.mouse.get_pos()
                    elif event.key == pygame.K_LEFTBRACKET:
                        if self.max_tps >= 100:
                            self.max_tps -= 100
                    elif event.key == pygame.K_RIGHTBRACKET:
                        self.max_tps += 100
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.environment.make_obstruction(event.pos)

            if self.simulating:
                self.update()
            self.draw()

            # Performance statistics
            if time()-self.sec_timer >= 1.0:
                self.sec_timer = time()
                self.tps_value = self.tps_counter
                self.tps_counter = 0
                self.fps_value = self.fps_counter
                self.fps_counter = 0

    def update(self):
        if self.max_tps == 0 or time() - self.tps_timer >= 1.0 / self.max_tps:
            self.tps_timer = time()
            self.tps_counter += 1
            self.population.update()

    def draw(self):
        if pygame.display.get_active() and time() - self.fps_timer >= 1.0 / self.max_fps:
            self.fps_timer = time()
            self.fps_counter += 1
            self.screen.fill((0, 0, 0))

            self.population.draw()
            self.environment.draw()
            self.debug.draw()

            pygame.display.flip()

if __name__ == "__main__":

    # Fix DPI
    import sys
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.user32.SetProcessDPIAware()
    Game()