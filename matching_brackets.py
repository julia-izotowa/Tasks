"""
We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones. The goal is to
check, whether brackets are in correct sequence. I.e. any opening bracket should have closing bracket of the same type
somewhere further by the string, and bracket pairs should not overlap, though they could be nested:

(a+[b*c] - {d/3})  - here square and curly brackets are nested in the round ones
(a+[b*c) - 17]     - here square brackets overlap with round ones which does not make sense

Input data will contain number of testcases in the first line.
Then specified number of lines will follow each containing a test-case in form of a character sequence.
"""


def matching_bracket(string):
    open_brackets = ['(', '[', '(', '<']
    close_brackets = [')', ']', ')', '>']
    raw_of_brackets = []

    for sign in string:
        if sign in open_brackets:
            raw_of_brackets.append(sign)
        elif sign in close_brackets and open_brackets.index(raw_of_brackets[-1]) == close_brackets.index(sign):
            raw_of_brackets.pop(-1)

    if len(raw_of_brackets) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    assert matching_bracket("4") == True
    assert matching_bracket("(((a * x) + [b] * y) + c") == False
    assert matching_bracket("(a + [b * c) - 17]") == False
    assert matching_bracket("{auf(zlo)men [gy<psy>] four{s}}") == True
