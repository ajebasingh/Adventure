import random

power = 0
life = 11
jump = 0

def welcome(name):
    """
    This function will welcome the user and provide game instructions
    :param name:
    :return:
    """
    print(f"Hi, {name}! You're finally up! You should check in with the admins of C.H.A.O.S. for a new mission.")

def power_level(level):
    powers = {
        1: "Immunity to Sarcasm... This sure looks useful!",
        2: "Plant Empathy! You can now hear plants asking to be watered!",
        3: "Resistance to Grass Damage! You can now touch grass!",
        4: "Dog Mindreader! You can now read a dog's thoughts!",
        5: "Stick to Walls! You can now stick to walls!",
        6: "Moonwalker! You can now moonwalk!",
        7: "3x Normal Appetite! Meals now cost 3x as much!",
        8: "...",
        9: "You didn't get a power this time, but you did get a pat on the back.",
        10: "Your levels are maxed out! You now have a golden aura and can speak Swahili!",
    }
    power_description = powers.get(level, "wow")
    print(f"You've received the power: {power_description}")

def process_action_3():
    global jump
    jump_delta = random.randint(-2, 3)
    jump = max(0, jump + jump_delta)
    print("boing, boing, boing, boing, boing...")
    if jump_delta > 0:
        print("All this jumping is exhausting!")
    elif jump_delta < 0:
        print("Your jumping prowess is increasing!")

def perform_action(action):
    global power, life
    if action == 1:
        power += random.randint(1, 3)
        power_level(power)
    elif action == 2:
        life -= random.randint(1, 3)
        print(f'You appear to be deathly allergic to even numbers. This may or may not be an issue moving forward. '
              f'Your current health is {life}')
    elif action == 3:
        process_action_3()

if __name__ == '__main__':
    welcome('PyCharm')

    while life > 0:
        try:
            action = int(input("Enter an action (1/2/3): "))
            if action not in (1, 2, 3):
                print("Invalid action. Please choose 1, 2, or 3.")
                continue

            perform_action(action)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nGame ended prematurely.")
            break

    if life <= 0:
        print(f"You have died. Your final score is... power: {power}, jump: {jump}")
