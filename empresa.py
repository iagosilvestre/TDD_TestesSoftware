class Empresa(object):

    def __init__(self, listaFuncionarios):
    	self.funcionarios = listaFuncionarios

    def getListaDeFuncionarios(self):
    	return self.funcionarios

    def adicionaFuncionario(self, funcionario):
    	self.funcionarios = self.funcionarios.append(funcionario)