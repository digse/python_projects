import time
import os

def main():
    hangman()

def hangman():
    hangman_word = input("Enter Hangman Word:\n").lower()
    letters = [" "]
    correct_letters = ""
    attempt_index = 0
    #attempt_num = 10

    attempt_num = [
        {"remaining": 11, "visual": ' '},
        {"remaining": 10, "visual": '|\n'},
        {"remaining": 9, "visual": '|\n|\n'},
        {"remaining": 8, "visual": '|\n|\n|\n'},
        {"remaining": 7, "visual": '|~\n|\n|\n'},
        {"remaining": 6, "visual": '|~~\n|\n|\n'},
        {"remaining": 5, "visual": '|~~o\n|\n|\n'},
        {"remaining": 4, "visual": '|~~o\n|  -\n|\n'},
        {"remaining": 3, "visual": '|~~o\n| >-\n|\n'},
        {"remaining": 2, "visual": '|~~o\n| >-<\n|  \n'},
        {"remaining": 1, "visual": '|~~o\n| >-<\n|  ^\n'}
    ]

    print('Hangman v1.0')
    print('*****************************')
    print(hangman_word)
    print('*****************************')

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"HANGMAN: {''.join(correct_letters)if correct_letters else 'Hit enter to reveal'}\n") #update to display masked word before the first loop iteration
        print(f'******************************************\n')
        print(f'Letter History: {''.join(letters)if letters else 'None'}')
        print(f'Attempts Remaining: {attempt_num[attempt_index]["remaining"]}\n{attempt_num[attempt_index]["visual"]}\n')
        print('*******************************************')

        correct_letters = ""
        guess = input("Enter a Letter:\n").lower()

        if guess.isalpha() and len(guess) <= 1:
            letters += guess
            attempt_index += 1
        else:
            print(f'{guess} is not valid.')
            time.sleep(0.5)

        for num, char in enumerate(hangman_word):
            if hangman_word[num] in letters:
                correct_letters += char
            else:
                correct_letters += "_"

        if guess in correct_letters and guess.isalpha():
            attempt_index -= 1

        if correct_letters == hangman_word:
            print(f'Good job, {hangman_word} is corret')
            break

        if attempt_index >= len(attempt_num):
            print("You lose!")
            break

main()
