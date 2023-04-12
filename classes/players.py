'''
Unicodedata module provides a tool to remove accentuation from characters.
'''
import unicodedata


# The Player class deals with how player's guesses are handled during game match.
#
class Player():

    # Constructor
    #
    def __init__(self):
        self.right_guesses = []
        self.wrong_guesses = []

    # Checks if all the letters of the word have been found by the player.
    #
    #  @param unicode_word
    #
    def checks_victory(self, unicode_word):
        victory = True
        for letter in unicode_word:
            if letter not in self.right_guesses:
                victory = False
                break
        return victory

    # Checks if the player's guess is valid.
    #
    #  @param guesses_made: list of right and wrong player guesses..
    #
    def validate_guess(self, guesses_made):
        while True:
            guess = input('Qual é o seu palpite?\n').upper()
            unicode_guess = unicodedata.normalize('NFD', guess)
            unicode_guess = unicode_guess.encode('ascii', 'ignore')
            unicode_guess = unicode_guess.decode('utf-8')

            if len(unicode_guess) == 0:
                print('Por favor, digite uma letra.\n')
            elif len(unicode_guess) != 1:
                print('Digite uma única letra.\n')
            elif unicode_guess in guesses_made:
                print('Você já tentou este palpite. Escolha outra letra.\n')
            elif unicode_guess == '-':
                return unicode_guess
            elif not unicode_guess.isalpha():
                print('Somente letras e hífens são palpites válidos.\n')
            else:
                print()
                return unicode_guess

    # Checks if the player wants to keep playing.
    #
    #  @return True: continuar
    #  @return False: parar
    #
    def play_again(self):
        while True:
            answer = input('Você quer jogar novamente? (S/N): ').upper()
            if answer not in ('S', 'N'):
                print('Digite "S" para sim ou "N" para não.\n')
            elif answer == 'S':
                return True
            else:
                self.farewell_message()
                return False

    # Clears the wrong and right guesses of the player to begin a new game match.
    #
    def reset_list(self):
        self.right_guesses.clear()
        self.wrong_guesses.clear()

    # Prints a farewell message to the player who chooses to leave the game.
    #
    def farewell_message(self):
        print('\nAté breve!\n')

    # Returns guesses made by the player.
    #
    #  @return Sum of right and wrong guesses.
    #
    def get_guesses(self):
        return self.right_guesses + self.wrong_guesses

    # Prints wrong and right guesses information in different fields.
    #
    def get_status(self):
        print('Palpites Certos: ')
        for letter in self.right_guesses:
            print(letter, end=' ')
        print('\n')

        print('Palpites Errados: ')
        for letter in self.wrong_guesses:
            print(letter, end=' ')
        print('\n')

    # Returns number of wrong guesses.
    #
    #  @return Number of wrong guesses.
    #
    def get_number_errors(self):
        return len(self.wrong_guesses)

    # Returns number of right guesses.
    #
    #  @return Number of right guesses.
    #
    def get_right_guesses(self):
        return self.right_guesses

    # Adds right guesses to the list.
    #
    def set_right_guess(self, guess):
        self.right_guesses.append(guess)

    # Adds wrong guesses to the list.
    #
    def set_wrong_guess(self, guess):
        self.wrong_guesses.append(guess)
