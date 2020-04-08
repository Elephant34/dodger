'''
A game- player dodge the falling blocks
'''
import pyglet
from pyglet.window import key
from assets.entities import player, timer

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
        main_batch.draw()

def update(dt):
    for enitity in enitity_list:
        enitity.update(dt)

window = Window(600, 600)
window.set_caption("Dodger")

main_batch = pyglet.graphics.Batch()

pressed = key.KeyStateHandler()
window.push_handlers(pressed)

enitity_list = []

player = player.Player(pressed, batch=main_batch)
enitity_list.append(player)

text = timer.Timer(batch=main_batch)
enitity_list.append(text)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()