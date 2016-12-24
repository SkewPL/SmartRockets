from pygame.math import Vector2
from random import random

def randomVector2():
    """
        Generates random normalized vector
    """
    return Vector2(random()*2-1, random()*2-1).normalize()