class Empresa(object):

    def __init__(self, listaFuncionarios):
        self.funcionarios = listaFuncionarios[:]

    def getListaDeFuncionarios(self):
        return self.funcionarios[:]

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def removeFuncionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def sortFuncionarios(self):
        self.funcionarios.sort()
    def __del__(self):
        return 1
