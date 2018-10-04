from empresa import *
import unittest

# a = c.Common(5)
# print(a.sharedMethod())

class TDD(unittest.TestCase):
    def setUp(self):
        self.a = Empresa()

    def teste_x(self):
        self.assertEqual(5, self.a.sharedMethod())

if __name__ == "__main__":
    unittest.main() # run all tests