class Empresa(object):

    def __init__(self, listaFuncionarios):
        self.funcionarios = listaFuncionarios[:]

    def __del__(self):
        return 1
        
    def getListaDeFuncionarios(self):
        return self.funcionarios[:]

    def sortFuncionarios(self):
        self.funcionarios.sort()
        return self.funcionarios[:]

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def removeFuncionario(self, funcionario):
        self.funcionarios.remove(funcionario)

