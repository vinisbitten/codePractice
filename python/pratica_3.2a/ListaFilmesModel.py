class Filme():
    def __init__(self, titulo, ano, nota):
        self._ano = ano
        self._nota = nota
        self._titulo = titulo
    
    def __str__(self):
        return self.titulo + ' (' + str(self.ano) + ') - ' + str(self.nota)

    @property
    def ano(self):
        return self._ano

    @property
    def nota(self):
        return self._nota
    
    @property
    def titulo(self):
        return self._titulo

class ListaFilmesModel():
    def __init__(self):
        self._listafilmes = []

    def __str__(self):
        saida = '--------------------' + '\n'
        for filme in self._listafilmes:
            saida += str(filme) + '\n'
        saida += '--------------------' + '\n'
        return saida
    
    '''adiciona um filme à lista'''
    def adiciona(self, filme):
        self._listafilmes.append(filme)

    '''pega o index de um filme na lista e o substitui por outro filme'''
    def atualiza(self, index, filme):
        self._listafilmes[index] = filme
    
    '''remove um filme da lista'''
    def remove(self, filme):
        self._listafilmes.remove(filme)

if __name__ == '__main__':

    novalista = ListaFilmesModel()

    filme1 = Filme("Don't Look Up", 2021, 7)
    filme2 = Filme("Jurassic Park", 1993, 8.5)
    filme3 = Filme("Pulp Fiction", 1994, 9)
    filme4 = Filme("The Velocipastor", 2017, 10)
    filme5 = Filme("A ilha do medo", 2010, 9)

    novalista.adiciona(filme1)
    novalista.adiciona(filme2)
    novalista.adiciona(filme3)
    novalista.adiciona(filme4)

    print(novalista)

    novalista.atualiza(2, filme5)

    print(novalista)

    novalista.remove(filme2)

    print(novalista)
