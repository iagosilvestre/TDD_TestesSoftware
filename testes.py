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
        self.ivan.__del__()
        self.ivan = None
        self.joao.__del__()
        self.joao = None
        self.listaDeFuncionarios = []      

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
        self.ocorrencia1 = Ocorrencia("Bug A", "Bug", "Alta", "Aberta", "ocorrencia1")
        self.projeto.addOcorrencia(self.ocorrencia1)
        self.assertEqual(["Bug A"], self.projeto.getOcorrencias())

    def testeAdicionaVariasOcorrencias(self):
        self.ocorrencia2 = Ocorrencia("Bug B", "Bug", "Alta", "Aberta", "ocorrencia2")
        self.ocorrencia1 = Ocorrencia("Bug A", "Bug", "Alta", "Aberta", "ocorrencia1")
        self.ocorrencia3 = Ocorrencia("Melhoria A", "Melhoria", "Alta", "Aberta", "ocorrencia3")
        self.projeto.addOcorrencia(self.ocorrencia1)
        self.projeto.addOcorrencia(self.ocorrencia2)
        self.projeto.addOcorrencia(self.ocorrencia3)
        self.assertEqual(["Bug A", "Bug B", "Melhoria A"], self.projeto.getOcorrencias())

    def testeVerificaOcorrenciaPorID(self):
        self.ocorrencia2 = Ocorrencia("Bug B", "Bug", "Alta", "Aberta", "ocorrencia2")
        self.ocorrencia1 = Ocorrencia("Bug A", "Bug", "Alta", "Aberta", "ocorrencia1")
        self.ocorrencia3 = Ocorrencia("Melhoria A", "Melhoria", "Alta", "Aberta", "ocorrencia3")
        self.projeto.addOcorrencia(self.ocorrencia1)
        self.projeto.addOcorrencia(self.ocorrencia2)
        self.projeto.addOcorrencia(self.ocorrencia3)
        #print(self.ocorrencia3.getNomeOcorrencia())
        #print(self.projeto.getOcorrenciaPorID(3).getNomeOcorrencia())
        self.assertEqual(self.ocorrencia3.getNomeOcorrencia(),self.projeto.getOcorrenciaPorID(3).getNomeOcorrencia())

class TDD_ocorrencia(unittest.TestCase):
    def setUp(self):
        self.ocorrencia1 = Ocorrencia("Bug A", "Bug", "Alta", "Aberta", "ocorrencia1")
        self.projeto = Projeto("Gerenciador de Tarefas", [])
        self.ivan = Funcionario("Ivan")

    def tearDown(self):
        self.ocorrencia1.__del__()
        self.ocorrencia1 = None
        self.projeto.__del__()
        self.projeto = None
        self.ivan.__del__()
        self.ivan = None

    def testeCriaOcorrencia(self):
        self.assertEqual("Bug A", self.ocorrencia1.getNomeOcorrencia())
        self.assertEqual("Bug", self.ocorrencia1.getTipoOcorrencia())
        self.assertEqual("Alta", self.ocorrencia1.getPrioridade())
        self.assertEqual("Aberta", self.ocorrencia1.getStatus())
        self.assertEqual("ocorrencia1", self.ocorrencia1.getResumo())

    def testeAtribuiFuncionario(self):
        self.projeto.atribuiOcorrencia(self.ocorrencia1, self.ivan)
        self.ivan.adicionaOcorrencia(self.ocorrencia1)
        self.assertEqual("Ivan", self.projeto.getOcorrenciaPorID(1).getResponsavel().getNome())
        self.assertEqual(1, self.ivan.getNumeroOcorrencias())
        self.assertTrue(self.ivan.checaOcorrencia(self.ocorrencia1.getNomeOcorrencia()))

    def testeModificaPrioridadeBaixa(self):
        self.ocorrencia1.setPrioridadeBaixa()
        self.assertEqual("Baixa", self.ocorrencia1.getPrioridade())

    def testeModificaPrioridadeMedia(self):
        self.ocorrencia1.setPrioridadeMedia()
        self.assertEqual("Media", self.ocorrencia1.getPrioridade())

    def testeModificaPrioridadeBaixa(self):
        self.ocorrencia2 = Ocorrencia("Bug B", "Bug", "Media", "Aberta", "ocorrencia2")
        self.ocorrencia2.setPrioridadeAlta()
        self.assertEqual("Alta", self.ocorrencia2.getPrioridade())

    def testeModificaResponsavel(self):
        self.joao = Funcionario("Joao")
        self.projeto.atribuiOcorrencia(self.ocorrencia1, self.ivan)
        self.projeto.getOcorrenciaPorID(1).setResponsavel(self.joao)
        self.joao.adicionaOcorrencia(self.projeto.getOcorrenciaPorID(1))
        self.assertEqual("Joao", self.projeto.getOcorrenciaPorID(1).getResponsavel().getNome())
        self.assertEqual(1, self.joao.getNumeroOcorrencias())
        self.assertTrue(self.joao.checaOcorrencia(self.ocorrencia1.getNomeOcorrencia()))

    def testeTerminaOcorrencia(self):
        self.ocorrencia1.finalizaOcorrencia()
        self.assertEqual("Fechada" ,self.ocorrencia1.getStatus())

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