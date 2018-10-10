class Projeto(object):
    def __init__(self, nomeProjeto, ocorrencias):
        self.nomeProjeto = nomeProjeto
        self.ocorrencias = ocorrencias[:]

    def __del__(self):
        return 1

    def addOcorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)

    def getOcorrencias(self):
        lista_ocorrencias = []
        for i in self.ocorrencias:
            lista_ocorrencias.append(i.nomeOcorrencia)
            lista_ocorrencias.sort()
        return lista_ocorrencias