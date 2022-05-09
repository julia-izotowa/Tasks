import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFibonacci(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = Fibonacci()

    def test_empty_fibonacci(self):
        self.assertListEqual([self.instance(n) for n in range(0)], [])

    def test_fibonacci(self):
        self.assertListEqual([self.instance(n) for n in range(5)], [0, 1, 1, 2, 3])

    def test_fibonacci_negative_value(self):
        self.assertListEqual([self.instance(n) for n in range(-4)], [])

    def test_fibonacci_one_element(self):
        self.assertListEqual([self.instance(n) for n in range(1)], [0])


class TestFormattedName(unittest.TestCase):

    def test_empty_first_name(self):
        with self.assertRaises(TypeError):
            formatted_name(last_name="Izotowa", middle_name="Olehivna")

    def test_empty_last_name(self):
        with self.assertRaises(TypeError):
            formatted_name(first_name="Yuliia", middle_name="Olehivna")

    def test_empty_middle_name(self):
        self.assertEqual(formatted_name("Yuliia", "Izotowa"), "Yuliia Izotowa")

    def test_full_name_title_function(self):
        self.assertEqual(formatted_name("yuliia", "izotowa"), "Yuliia Izotowa")


if __name__ == '__main__':
    unittest.main()
