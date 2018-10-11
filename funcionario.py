# Definicao da classe Funcionario
class Funcionario(object):
    def __init__(self, nome):
        self.nomeFuncionario = nome
        self.listaOcorrencias = []
        self.numOcorrencias = 0

    def __del__(self):
        return 1

    def getNome(self):
        return self.nomeFuncionario

    # Retorna quantas ocorrencias estao associadas ao Funcionario
    def getNumeroOcorrencias(self):
        return self.numOcorrencias

    def adicionaOcorrencia(self, ocorrencia):
        if(self.numOcorrencias < 10):
            self.listaOcorrencias.append(ocorrencia)
            self.numOcorrencias = self.numOcorrencias + 1

    # Verifica se o funcionario esta associado a certa ocorrencia
    def checaOcorrencia(self, nomeOcorrencia):
        for i in self.listaOcorrencias:
            if (i.getNomeOcorrencia() == nomeOcorrencia):
                return True
        return False