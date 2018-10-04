from empresa import *
import unittest

class TDD(unittest.TestCase):

    def setUp(self):
        self.angeloni = Empresa([])

    def teste_criaEmpresa(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_adicionaFuncionario(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.angeloni.adicionaFuncionario("Marcio")
        self.listaDeFuncionarios.append("Marcio")
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_adicionaFuncionarios(self):
        self.listaDeFuncionarios = ["Ivan", "Joao", "Marcio", "Otavio"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.listaDeFuncionarios.append("Thiago")
        self.angeloni.adicionaFuncionario("Thiago")
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def tearDown(self):
        self.angeloni.__del__()
        self.angeloni = None
    #def teste_adicionaFuncionarioNomeVazio(self):

if __name__ == "__main__":
    unittest.main() # run all tests