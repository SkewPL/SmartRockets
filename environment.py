from pygame import Rect
from pygame.math import Vector2
from pygame.draw import circle, rect

class Environment():

    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()
        self.target = (int(size[0]/2), 40)

        self.obstructions = []
        size = self.game.screen.get_size()
        self.obstructions.append(Rect(int(size[0] * 0.40), int(size[1] * 0.7), int(size[0] * 0.20), 20))
        self.obstructions.append(Rect(int(size[0] * 0.10), int(size[1] * 0.5), int(size[0] * 0.30), 20))
        self.obstructions.append(Rect(int(size[0] * 0.60), int(size[1] * 0.5), int(size[0] * 0.30), 20))
        self.obstructions.append(Rect(int(size[0] * 0.40), int(size[1] * 0.3), int(size[0] * 0.20), 20))
        self.newobs = None

    def make_obstruction(self, pos):
        if self.newobs:
            self.obstructions.append(Rect(self.newobs[0],self.newobs[1],pos[0]-self.newobs[0],pos[1]-self.newobs[1]))
            self.newobs = None
        else:
            self.newobs = pos

    def check_target(self, pos):
        '''
            Check if pos has reached target
        '''
        dist = pos.distance_to(Vector2(self.target))
        return dist <= 20

    def check_walls(self, pos):
        '''
            Check if pos has crushed into left, right or bottom wall
        '''
        size = self.game.screen.get_size()
        return pos.x < 0 or pos.x > size[0] or pos.y > size[1] or pos.y < 0

    def check_obstructions(self, pos):
        '''
            Check if pos has crushed into obstruction
        '''
        for obs in self.obstructions:
            if pos.x > obs.x and pos.x < obs.x+obs.w and pos.y > obs.y and pos.y < obs.y+obs.h:
                return True
        return False

    def draw(self):
        circle(self.game.screen, (0,100,255), self.target, 10)
        for obstruction in self.obstructions:
            rect(self.game.screen,(100,100,100), obstruction)