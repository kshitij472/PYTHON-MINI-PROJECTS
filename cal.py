import random
import string
lower_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def generate_password(length, include_uppercase, include_digits, include_symbols):
    characters = lower_letters
    
    if include_uppercase:
        characters += uppercase_letters
    if include_digits:
        characters += digits