from abc import ABC, abstractmethod
import datetime

class Treino(ABC):
    def __init__(self, modalidade):
        self._modalidade = modalidade
        self.__inicio = None
        self.__fim = None
    
    @abstractmethod
    def __str__(self):
        return f'Treino de <{self._modalidade}>'
    
    @abstractmethod
    def ritmo_medio(self):
        pass

    # Setter e Getter de inicio
    @property
    def inicio(self):
        return self.__inicio
    
    @inicio.setter
    def inicio(self, inicio):
        if type(inicio) == datetime.datetime:
            self.__inicio = inicio
        else:
            raise ValueError
    
    # Setter e Getter de fim
    @property
    def fim(self):
        return self.__fim
    
    @fim.setter
    def fim(self, fim):
        if type(fim) == datetime.datetime:
            self.__fim = fim
        else:
            raise ValueError

    # Getter duracao
    @property
    def duracao(self):
        tempo = self.__fim - self.__inicio
        return tempo.total_seconds()