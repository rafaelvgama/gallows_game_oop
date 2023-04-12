'''
Random module provides a random way to choose elements from a list
Unicodedata module provides a tool to remove accentuation from characters.
'''
import random
import unicodedata


# Word class defines how words and themes are handled in the game.
#
class Word():

    # Constructor.
    #
    def __init__(self):
        self.subjects = [
            'animais',
            'cores',
            'frutas',
            'objetos',
            'sobremesas',
        ]

    # Choose a random theme, then choose a random word inside the respective
    # theme, as well as the unicode characters and word size.
    #
    # @return list [theme,
    #               word,
    #               unicode word,
    #               word size]
    #
    def set_subject_word(self):
        subject = random.choice(self.subjects)
        file = 'subjects/' + subject + '.txt'
        words = []
        try:
            # listing = open(file, 'r', encoding='utf8')
            with open(file, 'r', encoding='utf8') as listing:
                for element in listing:
                    words.append(element.strip())
        except FileNotFoundError:
            print(f'\nOcorreu um problema na leitura do arquivo referente ao '
                  f'tema {subject.upper()}.')
        else:

            # listing.close()
            word = random.choice(words).upper()
            unicode_word = unicodedata.normalize('NFD', word)
            unicode_word = unicode_word.encode('ascii', 'ignore')
            unicode_word = unicode_word.decode('utf-8')
            size = len(word)
            result = []
            result.append(subject.upper())
            result.append(word)
            result.append(unicode_word)
            result.append(size)
            return result

    # Prints the secret word, hiding its characters, then revealing accordingly
    # player's right guesses.
    #
    # @param word: selected word.
    # @param unicode: selected word without accentuation.
    # @param size: number of letters of the word.
    # @param right_guesses: number of player's right guesses.
    #
    def draws_word(self, word, unicode, size, right_guesses):
        empty = '_' * size
        for i in range(size):
            if unicode[i] in right_guesses:
                empty = empty[:i] + word[i] + empty[i+1:]
        for element in empty:
            print(element, end=' ')
        print('\n')
