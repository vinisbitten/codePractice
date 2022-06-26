from treinomovel import TreinoMovel

class Usuario:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.treinos = []
        self.calorias = [4, 5, 6, 7, 8]
    
    def __str__(self):
        return f'{self.nome} - {self.idade} anos, {self.peso} kgs'

    def adiciona_treino(self, treino):
        self.treinos.append(treino)

    def imprime_calorias(self):
        for treino in self.treinos:
            if type(treino) == TreinoMovel:
                print(treino)
                print(f'Gasto calórico: {0.0175 * self.peso * treino.velocidade_media() * treino.duracao/60} cal/min')
            else:
                if self.peso >= 50 and self.peso <= 60:
                    cal = self.calorias[0]
                elif self.peso <= 70:
                    cal = self.calorias[1]
                elif self.peso <= 80:
                    cal = self.calorias[2]
                elif self.peso <= 90:
                    cal = self.calorias[3]
                elif self.peso <= 100:
                    cal = self.calorias[4]
                print(treino)
                print(f'Gasto calórico: {cal * treino.duracao/60} cal/min')
        print('\n')
