'''
Loads the resources and makes them accessable to all scripts
'''
import pyglet

pyglet.resource.path = ['assets/resources']
pyglet.resource.reindex()

images = {
    "player": pyglet.resource.image("player.png"),
    "block": pyglet.resource.image("block.png"),
}
