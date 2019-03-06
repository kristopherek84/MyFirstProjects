from sys import exit
from random import randint
from textwrap import dedent

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # be sure to print out the last scene
            current_scene.enter()



class Scene(object):
    pass



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


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship
            and destroed your entire crew. You are the last surviving
            member and you last mission is to get neutron
            bomb from Weapons Armory, put it in the bridge and
            blow the ship up after getting into an escape pod.)

            You're runnig down the central corridor to the Armory when
            a Gothon jumps out, has red scaly skin and sharp teeth
            dressed in evil clown costume.He's blocking the door
            to the Armory and his about to pull a weapon to blast you.
            """))


        action = input(">")

        if action == "shoot!":
            print(dedent("""
                    Quick on the draw you yank out blaster and aim it
                    at the Gothon. Your laser hits his costume but misses him.
                    This completly ruins his brand new costume his father
                    bought him, which makes him fly into an instant rage
                    and blast you repeatedly in the face until your dead.
                    Then he eats you.
                    """))
            return 'death'


        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer dodge, weave, slide
                right as the Gothon's blaster cranks
                past your head. In the middle of you acrobatics
                your foot slips and you bang your head on the
                wall and pass out. You wake up and shortly before
                you die the Gothon stomps on your head.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon in
                the academy. You tell the one Gothon joke
                LBHe zbgure vf fb sng, jura fur fvgf nebha
                fur fvgf nebhaq gur ubhfr. The Gothon stops and can't
                stop to lough. While he's loughing  you run up
                and shoot him in the head, and run to
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponAromory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory. Seek the room
            for more Gothons that might be hiding. You stand up
            and run to the corner of the room and find the box with
            neutron bomb. There's a keypad lock on the box and you need
            guess it. If you get the code wrong the lock closes
            forever.
            """))

        code = f"{randint(1,9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open.You grab the neutron bomb
                and run as fast as you can to the bridge
                where you must the bomb in right spot.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism locks forever.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with neutron destructor
            under your arm and suprise 5 Gothons who are scared enough
            to let you take control of the ship.
            Each of them has a clown costume.
            They havent pulled out their weapons out yet,
            as they see the active bomb under your arm
            and dont want to set it of.
            """))

        action = input(">")

        if action == "throw the bomb":
            print(dedent("""
                In panic you throw the bomb at the goup and make a leap
                for the door. Right as you throw it Gothon shoots you right
                in the back killing you. When you die you see another
                Gothon frantically trying to disarm the bomb.
                You die knowing they will blow up when it goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print (dedent("""
                You point your blaster at the bomb under your legs.
                The Gothons put their hands up and start to run. You then jump
                back punch the close button and blast the lock.
                Gothons can't get out. Now that the bomb is armed,
                you run to the escape pod to get off this ship
                """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscpePod(Scene):

    def enter(self):
        print (dedent("""
            You rush through the ship desperatly trying find the escape
            pod befor the whole ship explodes. Its likelely that Gothons are
            on yor ship. So you go the escape pods, and now pick one to take.
            Some of them could be demaged. but you dont have the time to
            check them out. There's 5 pods, which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into podand hit eject button.
                The pod easily slides out into space heading to
                planet below. As it flies to the planet, you turn
                to your back and see your ship implode then explode
                like a bright star, taking out the Gothon ship at a
                time. You won!
                """))
            return 'finished'
        else:
            print(dedent("""
                You jump into pod and hit the eject button.
                The pod escapes out into the void of space and
                implodes as the hull ruptures, crushing you
                to jam jelly.
                """))
            return 'death'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

            scenes = {
                'central_corridor': CentralCorridor(),
                'laser_weapon_armory': LaserWeaponAromory(),
                'the_bridge': TheBridge(),
                'escape_pod':EscpePod(),
                'death': Death(),
                'finished': Finished(),
            }

            def __init__(self, start_scene):
                self.start_scene = start_scene

            def next_scene(self, scene_name):
                val = Map.scenes.get(scene_name)
                return val

            def opening_scene(self):
                return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
