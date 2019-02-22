from mystery_word import *
from random import randint


def get_demon_words(words):
    """Given a list of words, choose a random word and return a list of every word of the same length"""
    mystery_word_length = len(words[randint(0,len(words))])
    demon_words = [word for word in words if len(word) == mystery_word_length]
    return demon_words


def narrow_word_bank(words, current_letter):
    """Takes the current list of words and an undercase letter and splits the bank into word families.  Returns a list of the largest word family"""
    word_families = {}
    for word in words:
        word_key = 0
        for i in range(len(word)):
            if current_letter == word[i]:
                word_key += 2**i
        if word_key in word_families:
            word_families[word_key].append(word)
        else:
            word_families[word_key] = [word]
        
    sorted_families = sorted(word_families, key = lambda k: len(word_families[k]), reverse = True)

    return word_families[sorted_families[0]]


if __name__ == "__main__":

    still_wants_to_play = True
    while still_wants_to_play:
        difficulty = get_difficulty()
        words = get_word_list(difficulty)
        demon_words = get_demon_words(words)
        word_progress = ["_" for e in demon_words[0]]
        guesses_left = 20
        guessed = []
        progress = [word_progress, guesses_left, guessed]
        win = False
        while progress[1] and not win:
            show_progress(progress)
            current_letter = get_letter(progress)
            demon_words = narrow_word_bank(demon_words, current_letter)
            progress = update_progress(demon_words[0], progress, current_letter)
            if "_" not in progress[0]:
                win = True

        show_progress(progress)
        if win:
            print("You won!")
        else:
            print(f"The word was {demon_words}.  Better luck next time :P")
        still_wants_to_play = get_play_again()