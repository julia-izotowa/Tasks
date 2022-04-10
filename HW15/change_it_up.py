"""
Create a function that takes a string as a parameter and does the following, in this order:

Replaces every letter with the letter following it in the alphabet (see note below)
Makes any vowels capital
Makes any consonants lower case
Note:

the alphabet should wrap around, so Z becomes A
in this kata, y isn't considered as a vowel.
So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)
"""
import string


def changer(s):
    alphabet = list(string.ascii_letters)
    new_string = ""
    for letter in s:
        if letter.isalpha():
            if letter.lower() == 'z':
                letter = 'a'
            else:
                letter = alphabet[alphabet.index(letter) + 1]

            if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
                letter = letter.upper()
            else:
                letter = letter.lower()
        new_string += letter
    return new_string


if __name__ == "__main__":
    assert changer('Cat30') == 'dbU30'
    assert changer('Alice') == 'bmjdf'
    assert changer('sponge1') == 'tqpOhf1'
    assert changer('Hello World') == 'Ifmmp xpsmE'
    assert changer('dogs') == 'Epht'
    assert changer('z') == 'A'
