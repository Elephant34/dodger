'''
A timer to count the elpsed time
'''
import pyglet

class Timer(pyglet.text.Label):
    '''
    A timer- this is function as the score see how long you can survive
    '''

    def __init__(self, **kwargs):
        '''
        Sets up the label
        '''
        super().__init__(**kwargs)

        self.num = 0.00
        self.text = str(self.num)

        self.font_family = "arial"
        self.font_size = 36

        self.x = 10
        self.y = 555
    
    def update(self, dt):
        '''
        Updates the time displayed
        '''

        self.num += dt
        self.text = str(round(self.num, 2))