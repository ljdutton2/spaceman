import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open("words.txt","r")
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):

    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
     '''
    wordGuess = ""
    for letter in secret_word:
        if letter in letters_guessed:
            wordGuess+=letter
        else:
            wordGuess+=("_")
    return wordGuess


def get_wrong_letters(letters_guessed,secret_word):
    wrongLetters = []
    for letter in letters_guessed:
        if letter not in secret_word:
            wrongLetters+=letter
    return wrongLetters







def is_guess_in_word(guess, secret_word):

    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess in secret_word:
        return True
    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    length= len(secret_word)
    alphabet = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r", "s","t","u","v","w","x","y","z"


    #TODO: show the player information about the game according to the project spec
    print("Spaceman Word Guessing Game")

    print ("The secret word has:",length,"letters")

    print ("You have 7 tries to guess the correct letters")


#TODO: Ask the player to guess one letter per round and check that it is only one letter

    running = True
    letters_guessed = []
    num_guesses = 0



    while running == True:
        letter = input("Please enter a letter: ")
        while len(letter) != 1 or letter in letters_guessed:
            letter = input("Please only enter one letter at a time, or enter a new letter:  ")



        letters_guessed += letter
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(letter,secret_word):
            print("That letter is correct!")
        else:
            print("Try again!")
            num_guesses += 1
        #lists the incorrect words so far
        print("The incorrect letters so far are: ", get_wrong_letters(letters_guessed,secret_word))





        #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))
        #TODO: check if the game has been won or lost

        #check why the y/n is not working
        if is_word_guessed(secret_word, letters_guessed):
            print("You win!")
            again = input("Do you want to play again? Enter (y/n):   ")

            if again.lower() == ("y"):
                secret_word = load_word()
                spaceman(secret_word)
            else:
                running = False

        if num_guesses >= 7:
            print("Thank you for playing!")
            print ("The secret word was",(secret_word))
            again = input("Do you want to play again?(y/n)")
            if again == "y":
                spaceman(load_word())
            if "y" not in again:
                running = False




#These function calls that will start the game

secret_word = load_word()
spaceman(secret_word)
