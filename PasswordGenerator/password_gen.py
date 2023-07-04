import random
import string

def generate_password(min_length,numbers=True,special_characters=True,capital_letters=True):
    letters_lowercase = string.ascii_lowercase
    letters_uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    characters = letters_lowercase
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    if capital_letters:
        characters+=letters_uppercase

    paswd = ""
    meet_criteria=False
    has_number=False
    has_special=False
    has_capital=False

    while not meet_criteria or len(paswd) < min_length:
        new_char=random.choice(characters)
        paswd+=new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        elif new_char in letters_uppercase:
            has_capital = True
        
        meet_criteria = True

        if numbers:
            meet_criteria=has_number
        if special_characters:
            meet_criteria=meet_criteria and has_special
        if capital_letters:
            meet_criteria=meet_criteria and has_capital
    return paswd

        