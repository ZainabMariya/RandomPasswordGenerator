import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # For uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # For lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def generate_password():
    option = input("Choose an option (1 for random password, 2 for encoding your own password): ")
    if option == "1":
        length = int(input("Enter the length of the random password: "))
        password = generate_random_password(length)
        print("Random Password:", password)
    elif option == "2":
        password = input("Enter the password you would like to encode: ")
        shift = int(input("Enter the shift key for Caesar cipher: "))
        encoded_password = caesar_cipher(password, shift)
        print("Encoded Password:", encoded_password)
    else:
        print("Invalid option!")


generate_password()
