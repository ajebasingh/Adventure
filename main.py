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
    print(f'Hi, {name}! ')


def power_level(level):
    if level == 1:
        print("You've received the power: Immunity to Sarcasm... This sure looks useful!")
    elif level == 2:
        print("")
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

    print(f"You have died. Your final score is {power}")
