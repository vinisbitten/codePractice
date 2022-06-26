import random
class Playlist:
    def __init__(self, music):
        self.__musicas = music.copy()

    def imprime(self):
        print('----------------')

        for i in range(len(self.__musicas)):
            print(self.__musicas[i])

        print('----------------')

    def adiciona(self, m):
        if m in self.__musicas:
            pass
        else:
            self.__musicas.append(m)

    def toca_proxima(self):
        print(f'Tocando agora: {self.__musicas[0]}')
        self.__musicas.pop(0)

    def embaralha(self):
        random.shuffle(self.__musicas)