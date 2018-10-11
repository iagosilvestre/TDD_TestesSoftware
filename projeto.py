class Projeto(object):
    def __init__(self, nomeProjeto, ocorrencias):
        self.nomeProjeto = nomeProjeto
        self.ocorrencias = ocorrencias[:]
        self.ID_ocorrencias = 1

    def __del__(self):
        return 1

    def addOcorrencia(self, ocorrencia):
        ocorrencia.setID(self.ID_ocorrencias)
        self.ID_ocorrencias = self.ID_ocorrencias+1
        self.ocorrencias.append(ocorrencia)

    def getOcorrencias(self):
        lista_ocorrencias = []
        for i in self.ocorrencias:
            lista_ocorrencias.append(i.nomeOcorrencia)
            lista_ocorrencias.sort()
        return lista_ocorrencias

    def getOcorrenciaPorID(self, ID):
        for i in self.ocorrencias:
            if(i != None):
                if(i.getID() == ID):
                    return i
        return None
