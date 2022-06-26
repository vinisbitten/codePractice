from abc import ABC, abstractmethod

class Recurso(ABC):

    @abstractmethod
    def __init__(self, nome):
        self.nome = nome
        self.n_tarefas = 0
        self.ocupado = False

    def reserva(self, n_tarefas):
        if self.ocupado == False:
            self.n_tarefas = n_tarefas
            self.ocupado = True
        
    @abstractmethod
    def processa(self):
        if self.n_tarefas > 0:
            self.n_tarefas -= 1

            if self.n_tarefas == 0:
                self.ocupado = False

            return True
        else:
            return False

    def libera(self):
        print(f'>Recurso {self.nome} com liberacao solicitada')
        
        if self.ocupado == True:
            self.n_tarefas = 0
            self.ocupado = False
            print(f'>Recurso {self.nome} liberado')
        else:
            print(f'>Recurso {self.nome} ja estava livre')
    
    def __repr__(self):
        return f'Recurso: {self.nome}, Tarefas: {self.n_tarefas}, Ocupado: {self.ocupado}'
    
    @property
    def tipo(self):
        return self.__class__.__name__