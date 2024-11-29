'''
AUTHOR: ServerLite
DATE: 11/29/24
'''

### LIBRARIES ###
import random

### PASSWORD GENERATOR CLASS ###
class PasswordGenerator:
    def __init__(self, length:int=5):
        self.__lower_letters = "abcdefghijklmnopqrstuvwxyz"
        self.__upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__special_characters = "!@#$%^&*()"
        self.__numbers = "1234567890"

        self.__length = length

    def generate_password(self, uppers=True,lowers=False,special=False,numbers=False):
        picking = ""

        # Checking to see what to pick based on user's choices
        if uppers: picking += self.__upper_letters
        if lowers: picking += self.__lower_letters
        if special: picking += self.__special_characters
        if numbers: picking += self.__numbers

        password = ""
        
        for index in range(self.__length): password += random.choice(picking)

        return password


if __name__ == "__main__":
    generator = PasswordGenerator(length=10)

    password = generator.generate_password(uppers=True, lowers=True, special=True, numbers=True)
    print(password)