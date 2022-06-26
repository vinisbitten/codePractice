from treino import *

class TreinoRepeticao(Treino):
    def __init__(self, modalidade, SecRep):
        Treino.__init__(self, modalidade)
        self.segundos_por_rep = SecRep
    
    def __str__(self):
        saida = super().__str__() + '\n'
        saida += self.inicio.strftime("%d/%m/%y, %H:%M") + '\n'
        saida += f'Duração: {self.duracao/60}\n'
        saida += f'Repetiçoes: {self.repeticoes()}\n'
        saida += f'Ritmo: {self.ritmo_medio()} seg/rep'
        return saida
    
    def repeticoes(self):
        return len(self.segundos_por_rep)
    
    def ritmo_medio(self):
        segundos = 0
        for sec in self.segundos_por_rep:
            segundos += sec
        return segundos/self.repeticoes()
    

    