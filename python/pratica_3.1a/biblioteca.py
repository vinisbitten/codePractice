from livro import Livro

class IsbnRepetido(Exception):
    pass
class ErrPar(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self._livros = []
    
    def cadastra(self, livro):
        '''Erro se o parâmetro não é um livro'''
        if type(livro) == Livro:
            for l in self._livros:
                if l._isbn == livro._isbn:
                    raise IsbnRepetido('ISBNRepetido: Há algo errado com o isbn de um dos livros')        
            self._livros.append(livro)
        else:
            raise ErrPar('ErroParametro: O parâmetro não é um livro')
    