from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def nasce(self):
        self.vivo = True

    @abstractmethod
    def morre(self):
        self.vivo = False

    @abstractmethod
    def emite_som(self):
        pass

class Mamifero(Animal):
    
    @abstractmethod
    def amamenta(self):
        pass

class Ave(Animal):

    @abstractmethod
    def voa(self):
        pass

class Gato(Mamifero):

    def __init__(self):
        super().__init__()

class Cachorro(Mamifero):

    def __init__(self):
        super().__init__()

class Ornitorrinco(Mamifero):

    def __init__(self):
        super().__init__()

class Pinguim(Ave):

    def __init__(self):
        super().__init__()

class Aguia(Ave):

    def __init__(self):
        super().__init__()