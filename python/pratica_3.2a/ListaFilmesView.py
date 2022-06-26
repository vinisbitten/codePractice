from tkinter import *

class ListaFilmesView:
    def __init__(self,root):
        self.root = root
        self.textos = {}
        self.entradas = {}
        self.botoes = {}
        self.lista = []
        self._inicializa()
    
    def _inicializa(self):
        '''frame com os textos, as entries e os botoes'''
        frame1=Frame(self.root, bd=10, relief=SUNKEN)
        frame1.pack(expand=True, fill=BOTH)

        '''textos'''
        self.textos['titulo']=Label(frame1, text='Título: ')
        self.textos['ano']=      Label(frame1, text='Ano: ')
        self.textos['nota']=    Label(frame1, text='Nota: ')

        '''entradas'''
        self.entradas['titulo']=Entry(frame1, width=20)
        self.entradas['ano']=   Entry(frame1, width=20)
        self.entradas['nota']=  Entry(frame1, width=20)

        '''botões'''
        self.botoes['ins']=  Button(frame1, text='Inserir')
        self.botoes['att']=Button(frame1, text='Atualizar')
        self.botoes['rmv']=  Button(frame1, text='Remover')

        '''ordenação'''
        self.textos['titulo'].grid(row=0, column=0, sticky='WE')
        self.entradas['titulo'].grid(row=0, column=1, columnspan= 3, sticky='WE')

        self.textos['ano'].grid(row=1, column=0,    sticky='wE')
        self.entradas['ano'].grid(row=1, column=1,  sticky='WE')
        self.textos['nota'].grid(row=1, column=2,   sticky='WE')
        self.entradas['nota'].grid(row=1, column=3, sticky='WE')

        self.botoes['ins'].grid(row=2, column=1, sticky='wE')
        self.botoes['att'].grid(row=2, column=2, sticky='wE')
        self.botoes['rmv'].grid(row=2, column=3, sticky='WE')

        '''configura linhas e colunas'''
        frame1.rowconfigure(0, weight=1)
        frame1.rowconfigure(1, weight=1)
        frame1.rowconfigure(2, weight=1)
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure(1, weight=1)
        frame1.columnconfigure(2, weight=1)

        '''frame com a listbox'''
        frame2=Frame(self.root, bg='white', bd=10, relief=SUNKEN)
        frame2.pack(expand=True, fill=BOTH)

        varLista = StringVar()
        varLista.set(self.lista)
        listview=Listbox(frame2, listvariable=varLista)
        listview.pack(expand=True, fill=BOTH)
if __name__ == "__main__":
    root=Tk()
    root.geometry('400x500')
    root.title('ListaFilmesView')

    lista = ListaFilmesView(root)

    lista.root.mainloop()