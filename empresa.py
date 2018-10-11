# Definicao da classe Empresa
class Empresa(object):

    def __init__(self, listaFuncionarios):
        self.funcionarios = listaFuncionarios[:]

    def __del__(self):
        return 1

    # Retorna lista com nomes dos funcionarios associados a Empresa
    def getListaDeFuncionarios(self):
        lista_nomes = []
        for i in self.funcionarios:
            lista_nomes.append(i.nomeFuncionario)
            lista_nomes.sort()
        return lista_nomes

    def adicionaFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def removeFuncionario(self, funcionario):
        self.funcionarios.remove(funcionario)
