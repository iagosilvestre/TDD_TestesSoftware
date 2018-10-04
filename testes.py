import classes as c
import unittest

# a = c.Common(5)
# print(a.sharedMethod())

class TDD(unittest.TestCase):
    def setUp(self):
        self.a = c.Common(5)

    def teste_x(self):
        self.assertEqual(5, self.a.sharedMethod())

    def teste_y(self):
        self.assertNotEqual(3, self.a.sharedMethod())

if __name__ == "__main__":
    unittest.main() # run all tests