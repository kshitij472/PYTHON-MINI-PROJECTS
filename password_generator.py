import random
import string

# Define character sets
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def generate_password(length, include_uppercase, include_digits, include_symbols):
    # Start with lowercase letters as the base
    characters = lowercase_letters

    # Add additional character sets based on user preferences
    if include_uppercase:
        characters += uppercase_letters
    if include_digits:
        characters += digits
    if include_symbols:
        characters += symbols

    # Ensure the password contains at least one character from each selected set
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase_letters))
    if include_digits:
        password.append(random.choice(digits))
    if include_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(characters) for _ in range(remaining_length))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def get_user_input():
    print("Welcome to Password Generator!!")
    print("-------------------------------")
    
    while True:
        try:
            length = int(input("Enter length of password: "))
            if length < 4:
                print("Password length must be at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_digits, include_symbols

def main():
    length, include_uppercase, include_digits, include_symbols = get_user_input()
    password = generate_password(length, include_uppercase, include_digits, include_symbols)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
