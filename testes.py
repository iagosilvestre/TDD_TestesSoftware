from empresa import *
from funcionario import *
from projeto import *
from ocorrencia import *
import unittest

class TDD_Empresa(unittest.TestCase):
    def teste_CriaEmpresa(self):
        self.angeloni = Empresa([])
        self.assertEqual([], self.angeloni.funcionarios)

class TDD_Funcionario(unittest.TestCase):
    def setUp(self):
        self.angeloni = Empresa([])
        self.listaDeFuncionarios = self.angeloni.getListaDeFuncionarios()
        self.ivan = Funcionario("Ivan")
        self.joao = Funcionario("Joao")
        self.listaDeFuncionarios.append(self.ivan.nomeFuncionario)
        self.listaDeFuncionarios.append(self.joao.nomeFuncionario)
        self.angeloni.adicionaFuncionario(self.joao)
        self.angeloni.adicionaFuncionario(self.ivan)

    def tearDown(self):
        self.angeloni.__del__()
        self.angeloni = None

    def teste_criaFuncionario(self):
        self.funcionario1 = Funcionario("Ivan")
        self.assertEqual(self.funcionario1.nomeFuncionario, "Ivan")

    def teste_adicionaFuncionario(self):
        self.listaDeFuncionarios.sort()
        self.assertEqual(["Ivan", "Joao"], self.angeloni.getListaDeFuncionarios())

    def teste_removeFuncionario(self):
        self.angeloni.removeFuncionario(self.joao)
        self.listaDeFuncionarios.remove("Joao")
        self.assertEqual(["Ivan"], self.angeloni.getListaDeFuncionarios())

class TDD_projeto(unittest.TestCase):
    def setUp(self):
        self.projeto = Projeto("Gerenciador de Tarefas", [])

    def tearDown(self):
        self.projeto.__del__()
        self.projeto = None
    
    def testeCriaProjeto(self):
        self.projeto = Projeto("Gerenciador", [])
        self.assertEqual("Gerenciador", self.projeto.nomeProjeto)
    
    def testeAdicionaOcorrencia(self):
        self.ocorrencia1 = Ocorrencia("Bug A")
        self.projeto.addOcorrencia(self.ocorrencia1)
        self.assertEqual(["Bug A"], self.projeto.getOcorrencias())

    def testeAdicionaVariasOcorrencias(self):
        self.ocorrencia2 = Ocorrencia("Bug B")
        self.ocorrencia1 = Ocorrencia("Bug A")
        self.ocorrencia3 = Ocorrencia("Melhoria A")
        self.projeto.addOcorrencia(self.ocorrencia1)
        self.projeto.addOcorrencia(self.ocorrencia2)
        self.projeto.addOcorrencia(self.ocorrencia3)
        self.assertEqual(["Bug A", "Bug B", "Melhoria A"], self.projeto.getOcorrencias())


if __name__ == "__main__":
    unittest.main() # run all tests


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