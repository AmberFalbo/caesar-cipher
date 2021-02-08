import re
import nltk

nltk.download('words', quiet=True)

from nltk.corpus import words


def encrypt(text, shift):
    encrypted_text = ""
    
    # This is assigning 1 to a and A
    lower_a = ord('a')
    upper_a = ord('A')

    # We start our for loo and create new characters to fill in the text whilst ignorting the numbers and exclamation marks.
    for char in text:
        num = ord(char)

        #both lowers checking if in betweening bottom and height of alphabet
        if lower_a <= num <= (lower_a + 26):
            base = lower_a
        elif upper_a <= num <= (upper_a + 26):
            base = upper_a
        else:
            base = None

        if base:
            num -= base
            num = (num + shift) % 26
            num += base
        encrypted_text += chr(num)
    return encrypted_text.strip()

def decrypt(encoded, shift):
    return encrypt(text, -shift)


def crack(encoded):
    pass

# remember .isalpha()


# if __name__=="__main__":
#     print(encrypt('abc', 1))
#     print(encrypt('bad wolf', 1))
#     print(encrypt('bad wolf 345', 1))
#     print(encrypt('bad wolf! 345', 3))
#     print(encrypt('123', 3))