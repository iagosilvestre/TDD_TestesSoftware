from empresa import *
import unittest

# a = c.Common(5)
# print(a.sharedMethod())

class TDD(unittest.TestCase):

    def teste_x(self):
        self.angeloni = Empresa()
        self.assertEqual(["Ivan"], self.angeloni.getListaDeFuncionarios())

if __name__ == "__main__":
    unittest.main() # run all tests