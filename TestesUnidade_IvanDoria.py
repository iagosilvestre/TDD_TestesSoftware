# Testes de Software - INE5448/08208
# Ivan Posca Doria - 13204824
# Tarefa 1 - Criacao de testes de unidade para biblioteca JodaTime ou similar
# Execucao dos testes via CLI: python "[nome do arquivo]" 
# |- Opcional: flag '-v' apos nome do arquivo p/ verbosidade

import unittest
import datetime
from datetime import timedelta

# Organizacao do teste de unidade:
# *Fixture setup: define todos os valores que devem ser utilizados durante o teste.
# *Exercise SUT: contem as chamadas dos metodos que estao sendo testados. 
# *Result verification: compara o resultado do metodo com o valor esperado.
# *Fixture teardown: finaliza o teste

# Em python, testes de metodos onde o resultado esperado eh uma excecao acontecem 
# dentro da chamada assertRaises, que recebe como argumentos a excecao esperada, 
# o metodo testado e os parametros utilizados na chamada.

# Testes #1, #2, #3, #4
class criaDatas(unittest.TestCase):
    # Fixture setup

    def teste_criaDataNatal(self):
        # Exercise SUT
        self.data_natal = datetime.date(2015,12,25)
        # Result verification
        self.assertEqual(self.data_natal.year,2015)
        self.assertEqual(self.data_natal.month,12)
        self.assertEqual(self.data_natal.day,25)        

    def teste_criaData_ArgumentoInvalido(self):
        # Exercise SUT
        # Result Verification
        self.assertRaises(ValueError, datetime.date, 2015,12,-1)

    def teste_criaData_MaisDe1ArgumentoInvalido(self):
        # Exercise SUT
        # Result Verification
        self.assertRaises(ValueError, datetime.date, 2015,0,-1)

    def teste_criaData_FaltaArgumento(self):
        # Exercise SUT
        # Result Verification
        self.assertRaises(TypeError, datetime.date, 2015,12)

    # Fixture teardown
 
#4, #5, #6, #7, #8, #9, #10, #11, #12
class operacoesComDatas(unittest.TestCase):
    # Fixture Setup
    def setUp(self):
        self.data = datetime.date(2015,1,1)
        self.dataFim2015 = datetime.date(2015,12,28)
    def teste_somaDias(self):
        # Exercise SUT
        self.data = self.data+timedelta(days=2)
        # Result verification
        self.assertEqual(self.data.day,3)
        self.assertEqual(self.data.month,1)
        self.assertEqual(self.data.year,2015)

    def teste_somaMes(self):
        # Exercise SUT
        self.data = self.data+timedelta(days=90)
        # Result verification
        self.assertEqual(self.data.day,1)
        self.assertEqual(self.data.month,4)
        self.assertEqual(self.data.year,2015)

    def teste_somaViraMes(self):
        # Exercise SUT
        self.data = self.data+timedelta(days=35)
        # Result verification
        self.assertEqual(self.data.day,5)
        self.assertEqual(self.data.month,2)
        self.assertEqual(self.data.year,2015)

    def teste_somaViraAno(self):
        # Exercise SUT
        self.dataFim2015 = self.dataFim2015+timedelta(days=5)
        # Result verification
        self.assertEqual(self.dataFim2015.day,2)
        self.assertEqual(self.dataFim2015.month,1)
        self.assertEqual(self.dataFim2015.year,2016)

    def teste_somaDataNegativa(self):
        # Exercise SUT
        self.data = self.data+timedelta(days=(-5))
        # Result verification
        self.assertEqual(self.data.day,27)
        self.assertEqual(self.data.month,12)
        self.assertEqual(self.data.year,2014)        

    def teste_subtracaoData(self):
        # Exercise SUT
        self.dataFim2015 = self.dataFim2015-timedelta(days=(5))
        # Result verification
        self.assertEqual(self.dataFim2015.day,23)
        self.assertEqual(self.dataFim2015.month,12)
        self.assertEqual(self.dataFim2015.year,2015)                

    def teste_subtracaoData_ViraAno(self):
        # Exercise SUT
        self.data = self.data-timedelta(days=(5))
        # Result verification
        self.assertEqual(self.data.day,27)
        self.assertEqual(self.data.month,12)
        self.assertEqual(self.data.year,2014)

    def teste_subtracaoDataNegativa(self):
        # Exercise SUT
        self.data = self.data-timedelta(days=(-5))
        # Result verification
        self.assertEqual(self.data.day,6)
        self.assertEqual(self.data.month,1)
        self.assertEqual(self.data.year,2015)

    # Fixture Teardown

#13, #14, #15, #16, #17, #18, #19
class criacaoHoras(unittest.TestCase):
    # Fixture Setup
    
    def teste_criaHora(self):
        # Exercise SUT
        self.hora = datetime.time(12,55,46)
        # Result verification
        self.assertEqual(self.hora.hour,12)
        self.assertEqual(self.hora.minute,55)
        self.assertEqual(self.hora.second,46)  

    def teste_criaHora_ArgumentoInvalido(self):
        # Exercise SUT
        # Result verification
        self.assertRaises(ValueError, datetime.time, 20,12,-20)

    def teste_criaHora_OutroArgumentoInvalido(self):
        # Exercise SUT
        # Result verification
        self.assertRaises(ValueError, datetime.time, 20,12,70)        

    def teste_criaHora_MaisDe1ArgumentoInvalido(self):
        # Exercise SUT
        # Result verification
        self.assertRaises(ValueError, datetime.time, 20,0,-20)

    def teste_criaHora_TodosArgumentosInvalidos(self):
        # Exercise SUT
        # Result verification
        self.assertRaises(ValueError, datetime.time, 25,70,75)

    def teste_criaHora_SemSegundos(self):
        # Exercise SUT
        self.hora = datetime.time(20,0)
        # Result verification
        self.assertEqual(self.hora.hour,20)
        self.assertEqual(self.hora.minute,0)
        self.assertEqual(self.hora.second,0) 

    def teste_criaHora_SoHora(self):
        # Exercise SUT
        self.hora = datetime.time(20)
        # Result verification
        self.assertEqual(self.hora.hour,20)
        self.assertEqual(self.hora.minute,0)
        self.assertEqual(self.hora.second,0)

    # Fixture Teardown

# Nota do aluno: A biblioteca datetime nao suporta soma entre objetos do tipo time,
# portanto estas serao realizadas em objetos do tipo datetime.

#20, #21
class criacao_DataEHora(unittest.TestCase):
    # Fixture Setup

    def teste_cria_DataEHora(self):
        # Exercise SUT
        self.dataEHora = datetime.datetime(2015,11,20,1,55,30)
        # Result Verification
        self.assertEqual(self.dataEHora.year, 2015)
        self.assertEqual(self.dataEHora.month,11)
        self.assertEqual(self.dataEHora.day,20)
        self.assertEqual(self.dataEHora.hour,1)
        self.assertEqual(self.dataEHora.minute,55)
        self.assertEqual(self.dataEHora.second,30)
    
    def teste_cria_DataEHoraInvalida(self):
        # Exercise SUT
        # Result Verification
        self.assertRaises(ValueError,datetime.datetime,2015,-11,20,1,55,30)
        
    # Fixture Teardown

#22, #23
class operacoes_DataEHora(unittest.TestCase):
    # Fixture Setup
    def setUp(self):
        self.dataEHora = datetime.datetime(2015,11,20,1,55,30)
    
    def teste_SomaMinutos(self):
        # Exercise SUT
        self.dataEHora = self.dataEHora+timedelta(minutes=7)
        # Result Verification
        self.assertEqual(self.dataEHora.minute,2)
        self.assertEqual(self.dataEHora.hour,2)

    def teste_SomaInvalida_Caractere(self):
        #Exercise SUT
        #Result Verification
        self.assertRaises(TypeError, datetime.datetime,2015,11,20,'a',55, 30)
    
    # Fixture Teardown

#24, #25, #26, #27, #28, #29
class compara_DataEHora(unittest.TestCase):
    # Fixture Setup
    def setUp(self):
        self.dataEHora = datetime.datetime(2015,11,20,1,55,30)
        self.dataEHora_mais1sec = datetime.datetime(2015,11,20,1,55,31)
        self.dataEHora_mais3dias = self.dataEHora_mais1sec+timedelta(days=3)
        self.dataEHora_menos3min = self.dataEHora-timedelta(minutes=3)
        self.dataEHora_menos1ano = datetime.datetime(2014,11,20,1,55,30)

    def teste_antes1(self):
        # Exercise SUT
        # Result Verification
        self.assertTrue(self.dataEHora < self.dataEHora_mais1sec)

    def teste_antes2(self):
        # Exercise SUT
        # Result Verification
        self.assertFalse(self.dataEHora > self.dataEHora_mais1sec)

    def teste_depois1(self):
        # Exercise SUT
        # Result Verification
        self.assertTrue(self.dataEHora_mais3dias > self.dataEHora_mais1sec)

    def teste_depois2(self):
        # Exercise SUT
        # Result Verification
        self.assertTrue(self.dataEHora > self.dataEHora_menos3min)

    def teste_confereDiferencaSegundos(self):
        # Exercise SUT
        self.interval = self.dataEHora_mais1sec - self.dataEHora
        # Result Verification
        self.assertEqual(self.interval, timedelta(seconds=1))

    def teste_confereDiferencaAno(self):
        # Exercise SUT
        self.interval = self.dataEHora - self.dataEHora_menos1ano
        # Result Verification
        self.assertEqual(self.interval, timedelta(days=365))

    # Fixture Teardown

#30
class comparaDatas(unittest.TestCase):
    # Fixture Setup
    def setUp(self):
        self.data = datetime.date(2015,12,25)
        self.data_mais1dia = self.data+timedelta(days=1)

    def teste_confereDiferencaDatas(self):
        # Exercise SUT
        self.interval = self.data_mais1dia - self.data
        # Result Verification
        self.assertTrue(self.interval, timedelta(days=1))

    # Fixture Teardown

# OBS: Os testes abaixo nao testam funcoes especificas da biblioteca datetime,
# e sim a funcao de atribuicao do proprio python

class compara_IgualdadeEntreObjeto_DataEHora(unittest.TestCase):
    # Fixture Setup
    def setUp(self):
        self.dataEHora1 = datetime.datetime(2015,11,20,1,55,30)
        self.dataEHora2 = datetime.datetime(2015,11,20,1,55,30)
        self.dataEHora3 = self.dataEHora2

    def teste_MesmoObjeto(self):
        # Exercise SUT
        # Result Verification
        self.assertIs(self.dataEHora2, self.dataEHora3)

    def teste_(self):
        # Exercise SUT
        # Result Verification
        self.assertIsNot(self.dataEHora1, self.dataEHora2)

    # Fixture Teardown

if __name__ == "__main__":
    unittest.main() # run all tests
