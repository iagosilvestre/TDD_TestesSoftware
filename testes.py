from empresa import *
import unittest

class TDD(unittest.TestCase):

    def teste_criaEmpresa(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())


    # def teste_listaDeFuncionarios(self):
    #     self.angeloni = Empresa()
    #     self.assertEqual(["Ivan"], self.angeloni.getListaDeFuncionarios())

if __name__ == "__main__":
    unittest.main() # run all tests