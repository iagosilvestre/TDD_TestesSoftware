class Empresa(object):

    def __init__(self):
        self.funcionarios = 0

    def getListaDeFuncionarios(self):
    	return self.funcionarios

    def sharedMethod(self):
        return self.x