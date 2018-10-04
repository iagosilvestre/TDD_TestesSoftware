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

    def teste_adicionaFuncionarios_ordemDiferente(self):
        self.listaDeFuncionarios.append("Thiago")
        self.listaDeFuncionarios.append("Maria")
        self.angeloni.adicionaFuncionario("Maria")
        self.angeloni.adicionaFuncionario("Thiago")

        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_removeFuncionario(self):
        self.angeloni.removeFuncionario("Joao")
        self.listaDeFuncionarios.remove("Joao")
        print(self.angeloni.getListaDeFuncionarios())
        print(self.listaDeFuncionarios)
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_removeOutroFuncionario(self):
        self.angeloni.removeFuncionario("Ivan")
        self.listaDeFuncionarios.remove("Joao")
        self.assertNotEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def tearDown(self):
        self.angeloni.__del__()
        self.angeloni = None


if __name__ == "__main__":
    unittest.main() # run all tests