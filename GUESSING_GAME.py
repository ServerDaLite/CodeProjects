'''
AUTHOR: ServerLite
DATE: 11/28/24
'''

### LIBRARIES ###
import random

### NUMBER GUESSING GAME CLASS ###
class GuessingGame:
    def __init__(self, min:int=1, max:int=100):
        self.__min = min
        self.__max = max
        self.__number_to_guess = random.randint(min, max)

        self.__number_of_tries = 0

    def getMin(self): return self.__min
    def getMax(self): return self.__max
    def getNumberToGuess(self): return self.__number_to_guess

    # Checks to see if the string is a digit.
    def __isDigit(self, string:str):
        digits = "1234567890"
        for character in string: 
            if character not in digits: return False
        return True

    # Run this function to start the game.
    def play(self):
        playing = True
        while playing:
            self.__number_of_tries += 1
            user_input = input(f"\nGuess a number from {self.__min} - {self.__max}: ")
            
            if self.__isDigit(user_input):
                user_input = int(user_input)
                if user_input > self.__number_to_guess:   # If user guess is too high
                    print("[RESULT] Too high, try again...")
                elif user_input < self.__number_to_guess: # If user guess is too low
                    print("[RESULT] Too low, try again...")
                else:                                     # The user guessed correctly.
                    print("[RESULT] Correct! Good Job!")
                    print(f"[RESULT] It took you {self.__number_of_tries} tries to get it right...")
                    print("\t - Try to get lower try count your next time playing.")
                    playing = False
            else:
                print(f"The input ({user_input}) is not a number.")

if __name__ == "__main__":
    GuessingGame().play()