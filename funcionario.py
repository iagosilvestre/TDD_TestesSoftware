from ocorrencia import *

class Funcionario(object):
    def __init__(self, nome):
        self.nomeFuncionario = nome
        self.listaOcorrencias = []
        self.numOcorrencias = 0

    def __del__(self):
        return 1

    def getNome(self):
        return self.nomeFuncionario

    def getNumeroOcorrencias(self):
        return self.numOcorrencias

    def adicionaOcorrencia(self, ocorrencia):
        self.listaOcorrencias.append(ocorrencia)
        self.numOcorrencias = self.numOcorrencias + 1

    def checaOcorrencia(self, nomeOcorrencia):
        for i in self.listaOcorrencias:
            if (i.getNomeOcorrencia() == nomeOcorrencia):
                return True
        return False