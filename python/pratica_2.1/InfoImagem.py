from InfoArquivo import InfoArquivo

class InfoImagem(InfoArquivo):
    def __init__(self, nome, tamanho, resolucao):
        InfoArquivo.__init__(self, nome, tamanho)
        self.resolucao = [resolucao[0], resolucao[1]]

    def __str__(self):
        return f'Imagem: {self.nome}, resolucao: [{self.resolucao[0]}, {self.resolucao[1]}] ({self.tamanho} MB)'

    def redimensiona(self):
        self.resolucao[0] = self.resolucao[0]/2
        self.resolucao[1] = self.resolucao[1]/2