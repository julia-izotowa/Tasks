"""
You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

Input:
If, you can read?

Output:
India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Note:

There are preloaded dictionary you can use, named NATO
The set of used punctuation is ,.!?.
Punctuation should be kept in your return string, but spaces should not.
Xray should not have a dash within.
Every word and punctuation mark should be seperated by a space ' '.
There should be no trailing whitespace
"""


def to_nato(words):
    translate_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
                      'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike',
                      'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra',
                      'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee',
                      'Z': 'Zulu', '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
                      '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '.': 'Decimal', '00': 'Hundred',
                      '000': 'Thousand'}

    words = list(words.replace(" ", "").upper())
    return " ".join([translate_dict.get(letter) if letter.isalnum() else letter for letter in words])


if __name__ == "__main__":
    assert to_nato(
        'If you can read') == "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"
    assert to_nato(
        'Did not see that coming') == "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"
    assert to_nato('.d?d!') == '. Delta ? Delta !'
