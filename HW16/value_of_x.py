"""
Jack's teacher gave him a ton of equations for homework. The thing is they are all kind of same so they are boring.

So help him by making a equation solving function that will return the value of x.

Test Cases will be like this:

# INPUT            # RETURN
'x + 1 = 9 - 2'    # 6
'- 10 = x'         # -10
'x - 2 + 3 = 2'    # 1
'- x = - 1'        # 1
All test cases are valid.
Every +, - and numbers will be separated by space.
There will be only one x either on the left or right.
x can have a - mark before it.
"""


def solve(eq: str) -> int:
    a, b = eq.replace('x', '0').split('=')
    x = eval(a) - eval(b)
    if '- x' in eq:
        x *= -1
    return x if eq.index('x') > eq.index('=') else -x


if __name__ == "__main__":
    assert solve('x + 1 = 9 - 2') == 6
    assert solve('x - 2 + 3 = 2') == 1
    assert solve('x = + 2 - 5 + 9') == 6
    assert solve('- 10 = x') == -10
    assert solve('- x = - 1') == 1
    assert solve('x - 0 + 0 = 0') == 0
