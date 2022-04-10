"""
You are a lonely frog.
You live on a coordinate axis.
The meaning of your life is to jump and jump..

Two actions are allowed:
forward: Move forward 1 unit.
double: If you at x point, then you can move to x*2 point.

Now, here comes your new task. Your starting point is x, the target point is y.
You need to jump to the target point with minimal steps. Please tell me, what's the minimal steps?
1 <= x <= 10, x < y <= 100000
"""


def jump_to(x, y):
    number = y
    steps_counter = 0
    while number != x:
        if number % 2 == 0 and number >= x * 2:
            number /= 2
        else:
            number -= 1
        steps_counter += 1
    return steps_counter


if __name__ == "__main__":
    assert jump_to(1, 8) == 3
    assert jump_to(1, 17) == 5
    assert jump_to(1, 15) == 6
    assert jump_to(3, 12) == 2
    assert jump_to(3, 16) == 3
    assert jump_to(3, 17) == 4
    assert jump_to(10, 19) == 9
