from sys import exit

print("Hi hello to my first game!")
name = input("What is your name?")
age = input("How old are you:")
weight = int(input("How much you weight?"))


def dead(why):
    print(why, "Good job!")
    exit(0)


def age_trap():
    if int(age) < 30:
        print("you can pass you are not to old")
        goldroom()
        #Here i have to make a function to the end of the game
    else:
        print("Sorry you are to old to play video games.")
        print("I cannot let you through, choose another route\n\n")
        start()


def test_trap():
    print("How many kilograms can elephant weigh?")
    smart = False

    while True:
        weigh = int(input("<"))
        if weigh == 5000:
            smart = True
            print("correct")
            goldroom()
        elif weigh < 5000:
            print("More")
        elif weigh > 5000:
            print("Less")
        else:
            dead(" You are not even trying? I wont keep you alive.")


def monsters():
    print("You enter a den of monsters")
        # I should work on it so it work us i intended
    monsters = ['bear', 'wolf', 'mice', 'kangaroo', 'rat', 'ginat ant']

    x = weight / 20
    x = int(x)
    counter = 0

    
        
    if len(monsters) > x:
        for i in range(x):
            print(f"you killed an {monsters[i]} with a rock")
        dead("You didnt have enough stones. Its happy hours for monsters")
    else:
        for i in monsters:
            print(f"you killed an {i} with a rock")
        print("congatulations. you killed all the monsters with the stones")
        goldroom()


def goldroom():
    print("You won")
    exit(0)

def start():
    print("You stand before a tall mountain.")
    print("There are three tunnels in front of you")
    print(" Which one do you choose: 1,2,3: ")

    tunnel = input(">")

    if "1" in tunnel:
        age_trap()
    elif "2" in tunnel:
        test_trap()
    elif "3" in tunnel:
        monsters()
    else: #I should later put this in a txt file
        dead("""
    You wander outside of the mountain thinking still
    that if you would make a choice, you would have
    to resign of 2 other options, so its not worth lossing
    2 of something you dont know for only 1 of this. Your dead.
    While you are dying you start to regret that you didnt make a choice.""")

start()
