"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting
with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is
rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""


def solution(roman):
    roman_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
    roman_exceptions = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    result = 0
    i = 0
    while i < len(roman):
        if roman[i:i + 2] in roman_exceptions:
            result += roman_exceptions.get(roman[i:i + 2])
            i += 2
        elif roman[i] in roman_symbols:
            result += roman_symbols.get(roman[i])
            i += 1
    return result


if __name__ == "__main__":
    assert solution('XXI') == 21
    assert solution('I') == 1
    assert solution('IV') == 4
    assert solution('MMVIII') == 2008
    assert solution('MDCLXVI') == 1666
