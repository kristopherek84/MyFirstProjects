from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configued".)
        print("Subclass it and implement enter")
        exit(1)


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter",
        "Such a luser",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


Class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship
            and destroed your entire crew. You are the last surviving
            member and you last mission is to get neutron
            bomb from Weapons Armory, put it in the bridge and
            blow the ship up after getting into an escape pod.)
"""

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

    while current scene != last scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene)

            # be sure to print out the last scene
        current_scene.enter()
