'''
This is the sprite controled by the player
'''
import pyglet
from pyglet.window import key
from assets.resources import loader

class Player(pyglet.sprite.Sprite):
    '''
    The player controled sprite character
    '''

    def __init__(self, pressed, **kawgs):
        '''
        Sets up the player
        '''
        super().__init__(img=loader.images["player"], **kawgs)
        self.scale = 0.4

        self.position = (0,20)

        self.pressed = pressed

        self.speed = 200
        self.move_x = 0
    
    def update(self, dt):
        '''
        Updates the player sprite
        '''

        if self.pressed[key.LEFT] or self.pressed[key.A]:
            self.move_x = -1
        elif self.pressed[key.RIGHT] or self.pressed[key.D]:
            self.move_x = 1
        else:
            self.move_x = 0
        
        self.x = self.x+(self.move_x*self.speed*dt)
        if self.x < 0-self.width:
            self.x = 600 - self.width
        elif self.x > 600:
            self.x = 0
    