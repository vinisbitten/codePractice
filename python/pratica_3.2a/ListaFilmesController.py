from ListaFilmesView import ListaFilmesView
from ListaFilmesModel import Filme, ListaFilmesModel
from tkinter import *

class ListaFilmesController:
    def __init__(self):
        self.model = None
        self.view = None

        self.root =Tk()
        self.root.title('ListaFilmesController')
        self.root.geometry('600x300')
        self.estado = 'ocioso'
        self.op = None
    
    def inicializa(self, model, view):
        self.model =model
        self.view = view
        self.view.lista = self.model.ListaFilmesModel()
        self._configura()

    def _configura(self):
        self.botoes['ins'] = lambda: self._processaEntrada('+')
        self.botoes['att'] = lambda: self._processaEntrada('=')
        self.botoes['rmv'] = lambda: self._processaEntrada('-')
        
    def _processaEntrada(self, par):
        if(par == '+'):
            self.model.adiciona()
        elif(par == '='):
            self.model.atualiza()
        elif(par == '-'):
            self.model.remove()
  
if __name__ == "__main__":
    controle = ListaFilmesController()
    model = ListaFilmesModel()
    view = ListaFilmesView()

    controle.inicializa(model, view)
    controle.executa()