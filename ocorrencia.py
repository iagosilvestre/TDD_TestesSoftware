class Ocorrencia(object):
    def __init__(self, nomeOcorrencia):
        self.nomeOcorrencia = nomeOcorrencia

    def __del__(self):
        return 1

    def getOcorrencia(self):
    	return self.nomeOcorrencia

