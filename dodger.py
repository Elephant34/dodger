'''
A game- player dodge the falling blocks
'''
import pyglet

class Window(pyglet.window.Window):
    '''
    The window class with custom draw function
    '''

    def __init__(self, width, height, **kawgs):
        '''
        Sets up the main window
        '''
        super().__init__(width, height, **kawgs)
    
    def on_draw(self):
        '''
        Overwrites the main draw function
        '''
        self.clear()

        # Draws all the other needed items

window = Window(600, 600)
window.set_caption("Dodger")

if __name__ == "__main__":
    pyglet.app.run()