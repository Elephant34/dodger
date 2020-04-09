'''
A game- player dodge the falling blocks
'''
import random
import math
import pyglet
from pyglet.window import key
from assets.entities import player, timer, block

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
    '''
    Updates all the entities so they can move
    '''
    # Based off decay function- probability increases over time
    # Stars in 1/72 with y asomote at 2
    chance = random.randint(
        1,
        round(70 * (math.e/2)**((-1/20)*float(timer.text))+2)
    )
    if chance == 1:
        falling = block.Block(batch=main_batch)
        falling.speed = random.uniform(
            30,
            70+(math.e**(float(timer.text)*9/100))
        )
        enitity_list.append(falling)
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

timer = timer.Timer(batch=main_batch)
enitity_list.append(timer)

enemy_list = []

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()