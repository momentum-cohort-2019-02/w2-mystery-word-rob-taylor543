from random import randint

def get_word_list(difficulty):
    """Opens the words.txt file, splits the words into a list, makes them all lower case and excludes ones outside of the difficulty range"""
    with open("words.txt") as words:
        words = words.read()
        words = words.split("\n")

    difficulty_words = []
    for word in words:
        if len(word) >= difficulty[0] and len(word) <= difficulty[1]:
            difficulty_words.append(word.casefold())

    return difficulty_words
    

def get_difficulty():
    """Asks user for input and returns a range of word lengths as a 2 element list"""
    difficulty = 0
    difficulties = [1,2,3]
    lowers_and_uppers = {1:[4,6], 2:[6,8], 3:[8,100]}
    while difficulty not in difficulties:
        try:
            difficulty = int(input("Enter a digit 1-3 to choose difficulty: "))
        except ValueError:
            print("Oops!  Please enter just a digit 1-3")
            continue
        if difficulty not in difficulties:
            print("Oops!  That is not within our range of difficulties")
    
    return  lowers_and_uppers[difficulty]


def show_progress(progress):
    """Prints how many guesses you have left and then the current word progress with blanks where you have not guessed it yet"""
    print(f"\nYou have {progress[1]} guesses left.")
    word_progress = ""
    for char in progress[0]:
        word_progress += char.upper() + " "
    print(word_progress + "\n")


def get_letter(progress):
    """Asks the user for a letter choice, makes sure that choice is valid and then returns that choice casefold"""
    letter_choice = ""
    while not letter_choice.isalpha():
        letter_choice = input("Letter choice: ").casefold()
        if not letter_choice.isalpha():
            print("Please only choose one letter with none of that symbol or number garbage.")
        elif letter_choice in progress[2]:
            print("You already guessed that letter!")
            letter_choice = ""
    return letter_choice


def update_progress(mystery_word, progress, current_letter):
    """Accepts the current progress as a list and the letter guess, returns the updated progress as a list (subtracts from guesses)"""
    didnt_find_one = True
    for i in range(len(progress[0])):
        if current_letter == mystery_word[i]:
            progress[0][i] = current_letter
            didnt_find_one = False
    if didnt_find_one:
        progress[1]-=1
    progress[2].append(current_letter)
    return progress


if __name__ == "__main__":

    difficulty = get_difficulty()
    words = get_word_list(difficulty)
    mystery_word = words[randint(0,len(words)-1)]
    word_progress = ["_" for e in mystery_word]
    guesses_left = 8
    guessed = []
    progress = [word_progress, guesses_left, guessed]
    win = False
    while progress[1] and not win:
        show_progress(progress)
        current_letter = get_letter(progress)
        progress = update_progress(mystery_word, progress, current_letter)
        if "_" not in progress[0]:
            win = True

    show_progress(progress)
    if win:
        print("You won!")
    else:
        print(f"The word was {mystery_word}.  Better luck next time :P")

