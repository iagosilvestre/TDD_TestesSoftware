class Funcionario(object):
    def __init__(self, nome):
        self.nomeFuncionario = nome

    def __del__(self):
        return 1

    def getNome(self):
        return self.nomeFuncionario