class Ocorrencia(object):
    def __init__(self, nomeOcorrencia, tipo, prioridade, status):
        self.nomeOcorrencia = nomeOcorrencia
        self.tipo = tipo
        self.prioridade = prioridade
        self.status = status

    def __del__(self):
        return 1

    def getNomeOcorrencia(self):
        return self.nomeOcorrencia

    def getTipoOcorrencia(self):
        return self.tipo

    def getPrioridade(self):
        return self.prioridade

    def getStatus(self):
        return self.status
