"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0
"""


def reverse(x: int) -> int:
    s = str(x)
    if not s[0].isdigit():
        x = int(s[0] + s[:0:-1])
    else:
        x = int(s[::-1])
    if pow(-2, 31) > x or x > pow(2, 31) - 1:
        return 0
    return x


if __name__ == "__main__":
    # assert reverse(321) == 123
    # assert reverse(-123) == -321
    # assert reverse(120) == 21
    assert reverse(1534236469) == 0
