class ErroTitulo(Exception):
    pass
class ErroAno(Exception):
    pass
class ErroISBN(Exception):
    pass

class Livro:
    def __init__(self, titulo = '', ano = 0, isbn = ''):
        self._titulo = titulo
        self._ano = ano
        self._isbn = isbn

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, ttl):
        '''ttl não pode ser string vazia'''
        if ttl == '':
            raise ErroTitulo('ExcecaoTituloLivro: Título do livro deve ser uma string não vazia')
        else:
            self._titulo = ttl

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        '''ano deve estar entre 1400 e 2100'''
        if ano >= 1400 and ano <= 2100:
            self._ano = ano
        else:
            raise ErroAno('O ano do livro deve estar entre 1400 e 2100')

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        '''ISBN deve conter pelo menos 6 caracteres'''
        if len(isbn) == 6:
            self._isbn = isbn
        else:
            raise ErroISBN('O código ISBN não contém 6 caracteres')