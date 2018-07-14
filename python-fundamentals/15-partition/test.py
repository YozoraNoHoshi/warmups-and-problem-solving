import unittest
# Click to add an import


class UnitTests(unittest.TestCase):

    def isEven(num):
        return num % 2 == 0

    def test_input_1(self):
        # Failure message:
        # expected partition([1, 2, 3, 4], isEven)
        # to equal [ [ 2, 4 ], [ 1, 3 ] ]
        self.assertEqual(partition([1, 2, 3, 4], isEven), [[2, 4], [1, 3]])

    def isString(el):
        return isinstance(el, str)

    def test_input_2(self):
        # Failure message:
        # expected partition(["hi", None, 6, "bye"], isString)
        # to equal [ [ "hi", "bye" ], [ None, 6 ] ]

        self.assertEqual(partition(["hi", None, 6, "bye"], isString), [
            ["hi", "bye"], [None, 6]])
