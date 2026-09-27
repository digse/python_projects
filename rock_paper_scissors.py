import random

"""
- this is my simple rock paper scissors game
- the design / naming conventions could be better but thats something i hope to make better in the future.
"""

def main():
    rps()

def rps():
    choice_1 = "r"
    choice_2 = "p"
    choice_3 = "s"

    choices = [choice_1, choice_2, choice_3]

    #player_two_choice = input(f"Rock (R), Paper (P), or Scissors (S)\nInput R, P or S\nPlayer 2: ").lower()

    quit_game = False

    while quit_game is False:
        player_one_choice = input(f"Rock (R), Paper (P), or Scissors (S)\nInput R, P or S\nPlayer 1: \n").lower()
        player_two_choice = random.choice(choices)

        print(f'******************************************\n')
        print(f'Player 1 Chose: {player_one_choice}')
        print(f'Player 2 Chose: {player_two_choice}\n')
        print(f'******************************************')

        if player_one_choice == choice_1 and player_two_choice == choice_1:
            print(f'Draw')
        elif player_one_choice == choice_2 and player_two_choice == choice_2:
            print('Draw')
        elif player_one_choice == choice_3 and player_two_choice == choice_3:
            print('Draw')
        elif player_one_choice == choice_1 and player_two_choice == choice_2:
            print('Player 2 beats Player 1 with Paper')
        elif player_one_choice == choice_2 and player_two_choice == choice_1:
            print('Player 1 beats Player 2 with Paper')
        elif player_one_choice == choice_3 and player_two_choice == choice_1:
            print('Player 2 beats Player 1 with Rock')
        elif player_one_choice == choice_1 and player_two_choice == choice_3:
            print('Player 1 beats Player 2 with Rock')
        elif player_one_choice == choice_3 and player_two_choice == choice_2:
            print('Player 1 beats Player 2 with Scissors')
        elif player_one_choice == choice_2 and player_two_choice == choice_3:
            print('Player 2 beats Player 1 with Scissors')
        else:
            print(f'{player_one_choice} is not R, P or S.')

        play_again_input = input("Play again? (y/n): ").lower()
        if play_again_input == "y":
            continue
        else:
            quit_game = True

main()
