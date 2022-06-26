from InfoImagem import InfoImagem

class InfoVideo(InfoImagem):
    def __init__(self, nome, tamanho, resolucao, duracao):
        InfoImagem.__init__(self, nome, tamanho, resolucao)
        self.duracao = duracao

    def __str__(self):
        return f'Video: {self.nome}, resolucao: [{self.resolucao[0]}, {self.resolucao[1]}], duracao: {self.duracao} ({self.tamanho} MB)'

    def excede_tamanho(self):
        if(self.tamanho > 1000 or self.resolucao[0] > 3840):
            return True
        else:
            return False