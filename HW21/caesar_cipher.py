"""
The action of a Caesar cipher is to replace each plaintext letter (plaintext letters are from 'a' to 'z' or
from 'A' to 'Z') with a different one a fixed number of places up or down the alphabet.

This program performs a variation of the Caesar shift. The shift increases by 1 for each character (on each iteration).

If the shift is initially 1, the first character of the message to be encoded will be shifted by 1, the second
character will be shifted by 2, etc...

Coding: Parameters and return of function "movingShift"
param s: a string to be coded

param shift: an integer giving the initial shift

The function "movingShift" first codes the entire string and then returns an array of strings containing the coded
string in 5 parts (five parts because, to avoid more risks, the coded message will be given to five runners, one
piece for each runner).

If possible the message will be equally divided by message length between the five runners. If this is not possible,
parts 1 to 5 will have subsequently non-increasing lengths, such that parts 1 to 4 are at least as long as when evenly
divided, but at most 1 longer. If the last part is the empty string this empty string must be shown in the resulting
array.

For example, if the coded message has a length of 17 the five parts will have lengths of 4, 4, 4, 4, 1. The parts
1, 2, 3, 4 are evenly split and the last part of length 1 is shorter. If the length is 16 the parts will be of
lengths 4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay at home since his part is the
empty string. If the length is 11, equal parts would be of length 2.2, hence parts will be of lengths 3, 3, 3, 2, 0.

You will also implement a "demovingShift" function with two parameters

Decoding: parameters and return of function "demovingShift"
an array of strings: s (possibly resulting from "movingShift", with 5 strings)

an int shift

"demovingShift" returns a string.
"""
import math
import string


def moving_shift(s, shift):
    alphabet = string.ascii_lowercase
    new_s = ''
    for letter in s:
        if letter.isalpha() and alphabet.find(letter.lower()) != -1:
            index = alphabet.index(letter.lower()) + shift
            if index >= 26:
                index %= 26
            if letter.isupper():
                new_s += alphabet[index].upper()
            else:
                new_s += alphabet[index]

        else:
            new_s += letter
        shift += 1

    chunks, chunk_size = len(new_s), math.ceil(len(new_s) / 5)
    message_list = [new_s[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    if len(message_list) == 4:
        message_list.append("")
    return message_list


def demoving_shift(s, shift):
    massage = ''.join([letter for letter in s])
    alphabet = string.ascii_lowercase
    new_s = ''
    for letter in massage:
        if letter.isalpha() and alphabet.find(letter.lower()) != -1:
            index = alphabet.index(letter.lower()) - shift
            if index < 0:
                index %= 26
            if letter.isupper():
                new_s += alphabet[index].upper()
            else:
                new_s += alphabet[index]

        else:
            new_s += letter
        shift += 1
    return new_s


if __name__ == "__main__":
    assert moving_shift("I should have known that you would have a perfect answer for me!!!",
                        1) == ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

    assert demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"],
                          1) == "I should have known that you would have a perfect answer for me!!!"
