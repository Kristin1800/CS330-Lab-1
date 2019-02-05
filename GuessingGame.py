# Kristin Goselin - Guessing Game Program
import random
guessesTaken = 0  #tracking the number of guesses the user takes
print("Hello Player, welcome to the Guessing Game! To begin enter in your name:")
name = input()  #Takes in the users inout and assigns it to name

number = random.randint(1, 10)  #creates a random number between 1 - 10
print("Nice to meet you", name, "! Lets get to the game, shall we? You have seven chances to guess between 0 and 10.")
print("May the odds be ever in your favor")
guesses_list = []  # stores guesses into a list
while guessesTaken < 6:  #creates a while statement that loops through while the number of guesses are less than 6

    print('Take a guess.')

    guess = input()
    guess = int(guess)
    guesses_list.append(guess)  #adds the user's guesses to the list

    guessesTaken = guessesTaken + 1  #creates a counter for guesses taken
    if guess < number:
        print('Your guest is too low.')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break  # breaks the loops when the correct number is guessed before seven chances
if guess == number:  #if statement for if the user is correct
    guessesTaken = str(guessesTaken)
    print('Good job ' + name + '! You won!')
    print('You guessed the number in ' + guessesTaken + ' guesses! Your guesses are below:')
    print(guesses_list)  #prints out guesses

if guess != number:  #if statement for if the user does not guess it in seven chances
    print(guesses_list)  #prints out guesses
    number = str(number)
    print('All of these guesses are incorrect. The correct number was ' + number)
