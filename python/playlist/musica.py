class Musica:
    def __init__(self, artista, titulo):
        self.__artista = f'{artista}'
        self.__titulo = f'{titulo}'

    def __str__(self):
        return f'{self.__artista} - {self.__titulo}'

    @property
    def artista(self):
        return self.__artista

    @property
    def titulo(self):
        return self.__titulo
    
    @artista.setter
    def artista(self, novo_artista):
        self.__artista = novo_artista

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo