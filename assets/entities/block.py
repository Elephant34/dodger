import random
import pyglet
from assets.resources import loader


class Block(pyglet.sprite.Sprite):
    '''
    Falling block which is the thing the player dodges
    '''

    def __init__(self, **kwargs):
        '''
        Sets up the block
        '''
        super().__init__(img=loader.images["block"], **kwargs)

        self.scale = random.uniform(0.1, 1)
        self.x = random.uniform(-self.width+1, 599+self.width)
        self.y = 600

        self.speed = 10

    def update(self, dt):
        '''
        Moves the blocks downward
        '''

        self.y -= self.speed * dt