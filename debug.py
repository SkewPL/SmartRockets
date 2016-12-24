from pygame.font import *

class Debug():

    def __init__(self, game):
        self.game = game
        self.font = SysFont('monospace', 16)
        self.textoff = 0

    def text(self, *msg):
        label = self.font.render(' '.join(map(str, msg)), 1, (255, 255, 255))
        self.game.screen.blit(label, (10, 10+self.textoff))
        self.textoff += 18

    def draw(self):
        self.textoff = 0
        self.text("FPS:", self.game.fps_value, "TPS:", self.game.tps_value, "MaxTPS:", self.game.max_tps)
        self.text("Generation:",self.game.population.generation, "MaxFit:", self.game.population.maxfit)
        self.text("Target achieved in:", self.game.population.target_achieved)
        self.text("LifeCount:", self.game.lifecount, "Living:",self.game.population.living)