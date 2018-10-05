from empresa import *
from funcionario import *
import unittest

class TDD_Empresa(unittest.TestCase):
    def teste_CriaEmpresa(self):
        self.angeloni = Empresa([])
        self.assertEqual([], self.angeloni.funcionarios)

class TDD_Funcionario(unittest.TestCase):
    def setUp(self):
        self.angeloni = Empresa([])
        self.listaDeFuncionarios = self.angeloni.getListaDeFuncionarios()

    def tearDown(self):
        self.angeloni.__del__()
        self.angeloni = None

    def teste_criaFuncionario(self):
        self.funcionario1 = Funcionario("Ivan")
        self.assertEqual(self.funcionario1.nome, "Ivan")

    def teste_adicionaFuncionario(self):
        self.ivan = Funcionario("Ivan")
        self.joao = Funcionario("Joao")
        self.listaDeFuncionarios.append(self.ivan.nome)
        self.listaDeFuncionarios.append(self.joao.nome)
        self.angeloni.adicionaFuncionario(self.ivan)
        self.angeloni.adicionaFuncionario(self.joao)
        print(self.angeloni.getListaDeFuncionarios())
        self.assertEqual(["Ivan", "Joao"], self.angeloni.getListaDeFuncionarios())



# class TDD_Empresa_Funcionario(unittest.TestCase):

#     def setUp(self):
#         self.angeloni = Empresa([])
#         self.angeloni.adicionaFuncionario("Ivan")
#         self.angeloni.adicionaFuncionario("Joao")
#         self.listaDeFuncionarios = ["Ivan", "Joao"]

#     def teste_adicionaFuncionario(self):
#         self.angeloni.adicionaFuncionario("Marcio")
#         self.listaDeFuncionarios.append("Marcio")
#         self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionariosOrganizada())

#     def teste_adicionaFuncionarios_ordemDiferente(self):
#         self.listaDeFuncionarios.append("Thiago")
#         self.listaDeFuncionarios.append("Maria")
#         self.angeloni.adicionaFuncionario("Maria")
#         self.angeloni.adicionaFuncionario("Thiago")

#         self.listaDeFuncionarios.sort()
#         self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionariosOrganizada())

#     def teste_removeFuncionario(self):
#         self.angeloni.removeFuncionario("Joao")
#         self.listaDeFuncionarios.remove("Joao")
#         self.assertEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

#     def teste_removeOutroFuncionario(self):
#         self.angeloni.removeFuncionario("Ivan")
#         self.listaDeFuncionarios.remove("Joao")
#         self.assertNotEqual(self.listaDeFuncionarios, self.angeloni.getListaDeFuncionarios())

#     def tearDown(self):
#         self.angeloni.__del__()
#         self.angeloni = None

if __name__ == "__main__":
    unittest.main() # run all tests