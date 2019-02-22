from mystery_word import *
from demon_words import *


if __name__ == "__main__":

    for i in range(4, 15):
        with open("words.txt") as words:
            words = words.read()
            words = words.split("\n")

        i_length_words = []
        for word in words:
            if len(word) == i:
                i_length_words.append(word.casefold())

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        best_choices = []
        words_size = []

        while not len(i_length_words) == 1:
            alphabet_choices = {}
            for char in alphabet:
                narrower_words = narrow_word_bank(i_length_words, char)
                alphabet_choices[char]=narrower_words

            choices = sorted(alphabet_choices, key = lambda k: len(alphabet_choices[k]))
            best_choice = choices[0]
            i_length_words = narrow_word_bank(alphabet_choices[choices[0]], best_choice)

            best_choices.append(choices[0])
            words_size.append(len(alphabet_choices[best_choice]))
        print(f"for a word of length {i}, you should choose {best_choices}, you will end up with: {i_length_words}")
        print(f"the size of the pool after each guess is {words_size}")