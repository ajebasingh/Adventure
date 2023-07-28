# Adventure text based game!
import random

power = 0
life = 11


def welcome(name):
    """
    This function will welcome the user, and provide game instructions
    :param name:
    :return:
    """
    print(f'Hi, {name}! Your finally up! You should check in with the higher-ups of Chaos for a new mission.')


def power_level(level):
    if level == 1:
        print("You've received the power: Immunity to Sarcasm... This sure looks useful!")
    elif level == 2:
        print("You've received the power: Plant Empathy! You can now hear plants asking to be watered!")
    elif level == 3:
        print("You've received the power: Resistance to Grass Damage! You can now touch grass!")
    elif level == 4:
        print("You've received the power: Dog Mindreader! You can now read a dog's thoughts!")
    elif level == 5:
        print("You've received the power: Stick to Walls! You can now stick to walls!")
    elif level == 6:
        print("You've received the power: Moonwalker! You can now moonwalk!")
    elif level == 7:
        print("You've received the power: 3x Normal Appetite! Meals now cost 3x as much!")
    elif level == 8:
        print("You've received the power: ...")
    elif level == 9:
        print("You didn't get a power this time, but you did get a pat on the back.")
    elif level == 10:
        print("Your levels are maxed out! You now have a golden aura and can speak Swahili!")
    else:
        print("wow")


def perform_action(action):
    if action == 1:
        global power
        power += random.randint(1, 3)
        power_level(power)
    elif action == 2:
        global life
        life -= random.randint(1, 3)
        print(f'You appear to be deathly allergic to even numbers. This may or may not be an issue moving forward. '
              f'Your current health is {life}')
    elif action == 3:
        global jump
        jump+= random.randint(-2, 3)
        print("boing, boing, boing, boing, boing...")
        
    else:
        1 == ("slot 1")
        2 == ("slot 2")
        3 == ("slot 3")
        print("you can only use 1,2 and 3")

# Run Adventure!
if __name__ == '__main__':
    welcome('PyCharm')
    action = int(input("Enter an action: "))

    while action > 0:
        perform_action(action)
        action = int(input("Enter an action: "))

    print(f"Your final score is: {power} (1, 1000)")
