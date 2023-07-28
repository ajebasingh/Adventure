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
    print(f'Hi, {name}!  ')


def perform_action(action):
    if action == 1:
        global power
        power += random.randint(1, 3)
    if action == 2:
        global life
        life -= random.randint(1, 3)
    print("You have lost a heart.")

# Run Adventure!
if __name__ == '__main__':
    welcome('PyCharm')
    action = int(input("Enter an action: "))

    while action != 0:
        perform_action(action)
        action = int(input("Enter an action: "))

    print(f"Your final score: {power}")

