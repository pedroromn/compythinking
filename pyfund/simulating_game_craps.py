# simulating_game_craps.py
import random

def roll_dice():
    """ Roll two dice and return their face values as a tuple """
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    return (die1, die2) # valores de las caras en una tupla

def display_dice(dice):
    """ Display one roll of the two dice. """
    die1, die2 = dice
    print(f"die1: {die1} - die2: {die2}")
    print(f"Player rolled {die1} + {die2} = {sum(dice)}")

def simulation_craps():
    """ Simulating game craps """
    dice = roll_dice()
    display_dice(dice)
    sum_of_dice = sum(dice)

    if sum_of_dice in (7, 11):
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):
        game_status = 'LOST'
    else:
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        print(f"Point is {my_point}")

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice() # Nuevo lanzamiento de dados
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point: # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:
            game_status = 'LOST'
        else:
            my_point = sum_of_dice
            print(f"Point is {my_point}")

    return game_status

def main():
    print("Similation game craps init: ")
    game_status = simulation_craps()

    if game_status == 'WON':
        print("\nPlayer wins!!")
    else:
        print("\nPlayor loses - :S")


if __name__ == "__main__":
    main()
