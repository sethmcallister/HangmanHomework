from requests import Session
import thread

session = Session()

word = session.get('http://setgetgo.com/randomword/get.php').text

correctGuesses = []

lives = 10


def printWord():
    word1 = ""
    for character in word:
        if correctGuesses.__contains__(character):
            word1 += character
        else:
            word1 += "_"

    print word1
    return word1


def askForGuess():
    global lives
    character = raw_input("Please guess a character")
    if not word.__contains__(character):
        print "Whoops! please try again!"
        print "you have {} remaining lives!".format(str(lives))
        lives -= 1
        if lives == 0:
            print "You have run out of lives! Better luck next time"
            quit()
            return
        askForGuess()
        return

    correctGuesses.append(character)
    print "Correct! You have guessed a letter correctly, so far you have found!"
    soFar = printWord()
    if not soFar.__contains__("_"):
        print "Congratulations! You have guess the word! It was {}".format(word)
    askForGuess()
    return


printWord()
thread.start_new_thread(askForGuess(), 0)
