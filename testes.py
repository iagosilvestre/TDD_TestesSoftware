from empresa import *
import unittest

class TDD(unittest.TestCase):

    def teste_criaEmpresa(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    def teste_adicionaFuncionario(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.angeloni.adicionaFuncionario("Marcio")
        self.listaDeFuncionarios = self.listaDeFuncionarios.append("Marcio")
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

def teste_adicionaFuncionarios(self):
        self.listaDeFuncionarios = ["Ivan", "Joao"]
        self.angeloni = Empresa(self.listaDeFuncionarios)
        self.angeloni.adicionaFuncionario("Marcio")
        self.angeloni.adicionaFuncionario("Jose")
        self.listaDeFuncionarios = self.listaDeFuncionarios.append("Marcio")
        self.listaDeFuncionarios = self.listaDeFuncionarios.append("Jose")
        self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

    # def teste_listaDeFuncionarios(self):
    #     self.angeloni = Empresa()
    #     self.assertEqual(["Ivan"], self.angeloni.getListaDeFuncionarios())

if __name__ == "__main__":
    unittest.main() # run all tests