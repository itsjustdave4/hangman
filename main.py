import random
from words import words

while True:
    # tries to guess the word
    tries = 10
    # create a list with all the chars from a random word within words.py
    chosenWord = random.choice(words)
    wordList = list(chosenWord)
    # count the length
    charCount = len(wordList)
    # create a list of underscores with the same length
    hiddenWord = []
    wrongGuesses = []
    for charCount in wordList:
        hiddenWord.append("_")
    # shows the length of the word as an integer
    print("try to guess: ")
    # shows the list of underscores
    print(hiddenWord)

    # --- playing as long as tries are not 0 ---
    while tries > 0:
        # win the game if both lists are identical
        if wordList == hiddenWord:
            print("YOU WIN!!!")
            print("The word is: " + chosenWord)
            playAgain = input('Play again? (Y/N) ').upper()
            if playAgain == 'Y':
                break
            else:
                exit()
        else:
            # retrieve the guessed char and set it as a variable
            guess = input("enter your guess: ").lower()
            # check if chosen word contains the guessed char if yes -> print the char and a message
            if guess in wordList:
                print(guess + " is correct!")
                # set i to the position of the guessed char
                i = wordList.index(guess)
                # replace an underscore with the correct char on the same position as in wordList
                hiddenWord = [guess if guess == wordList[i] else hiddenWord[i] for i in range(len(wordList))]
                # show the updated hiddenWord
                print(hiddenWord)
                print("wrong guesses:" + str(wrongGuesses))
                # if no -> print the char and a message and reduce the remaining tries by one
            else:
                print(guess + " is wrong!")
                tries = tries - 1
                wrongGuesses.append(guess)
                print("remaining tries: " + str(tries))
                print(hiddenWord)
                print("wrong guesses:" + str(wrongGuesses))
                # check if tries are 0 and if yes print a message, the chosen word and exit the code
                if tries == 0:
                    print("you lose! the word was: " + chosenWord)
                    playAgain = input('you want to play again? (y/n) ').lower()
                    if playAgain == 'y':
                        break
                    else:
                        exit()
