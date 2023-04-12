'''
The os module provides a way of using operating system dependent functionality.
'''
import os

from classes.hanged import Hanged
from classes.words import Word
from classes.players import Player


##########
# Functions
##########

# Clears the terminal screen.
#
def screen_cleaner():
    os.system('clear')


# Prints programs headers information.
#
def header():
    print('''
=====================================================
                    JOGO DA FORCA
=====================================================
''')


# Prints game match main information on screen.
#
def draw_game():
    screen_cleaner()
    header()
    print(f'O tema desta rodada é {subject} '
          f'e a palavra tem {secret_size} letras.')
    hanged.draw_gallows(player.get_number_errors())
    word.draws_word(
        secret,
        unicode,
        secret_size,
        player.get_right_guesses()
    )
    player.get_status()
    print(f'Tentativas erradas restantes: '
          f'{hanged.get_error_limit() - player.get_number_errors()}\n')


##########
# Main
##########
try:
    screen_cleaner()
    header()
    running = True
    while running == True:
        start = input('Você quer iniciar uma rodada? (S/N): ').upper()
        if (start != 'S') and (start != 'N'):
            print('Digite "S" para sim ou "N" para não.\n')
        elif start == 'S':
            word = Word()
            player = Player()
            hanged = Hanged()
            game_match = word.set_subject_word()
            subject = game_match[0]
            secret = game_match[1]
            unicode = game_match[2]
            secret_size = game_match[3]
            while running == True:
                draw_game()
                palpite = player.validate_guess(player.get_guesses())
                if palpite in unicode:
                    player.set_right_guess(palpite)
                    if player.checks_victory(unicode):
                        draw_game()
                        print(f'Correto! A palavra é {secret}. '
                              'Parabéns!\n')
                        running = False
                else:
                    player.set_wrong_guess(palpite)
                    if player.get_number_errors() == hanged.get_error_limit():
                        draw_game()
                        print('Não foi dessa vez. Você alcançou o limite de '
                              f'tentativas. A palavra era {secret}.\n')
                        running = False

                if not running and player.play_again():
                    player.reset_list()
                    game_match = word.set_subject_word()
                    subject = game_match[0]
                    secret = game_match[1]
                    unicode = game_match[2]
                    secret_size = game_match[3]
                    running = True
        else:
            player = Player()
            player.farewell_message()
            running = False
except KeyboardInterrupt:
    screen_cleaner()
    print('\n\nO jogador interrompeu a partida.\n')
