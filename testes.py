from empresa import *
import unittest

class TDD(unittest.TestCase):

    def setUp(self):
        self.angeloni = Empresa([])
        self.angeloni.adicionaFuncionario("Ivan")
        self.angeloni.adicionaFuncionario("Joao")
        self.listaDeFuncionarios = ["Ivan", "Joao"]

    def teste_adicionaFuncionario(self):
        self.angeloni.adicionaFuncionario("Marcio")
        self.listaDeFuncionarios.append("Marcio")
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_adicionaFuncionarios(self):
        self.listaDeFuncionarios.append("Thiago")
        self.listaDeFuncionarios.append("Maria")
        self.angeloni.adicionaFuncionario("Maria")
        self.angeloni.adicionaFuncionario("Thiago")
        self.assertEqual(self.listaDeFuncionarios.sort(), self.angeloni.getListaDeFuncionarios().sort())

    def tearDown(self):
        self.angeloni.__del__()
        self.angeloni = None


if __name__ == "__main__":
    unittest.main() # run all tests