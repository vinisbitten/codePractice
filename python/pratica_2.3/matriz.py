class Matriz:
    '''Representa uma matriz de tamanho nl x nc.'''

    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        '''Inicializa a matriz com 0s.'''
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __repr__(self):
        '''Retorna a matriz em formato de str''' 
        s = ''
        for i in range(self._nl):
            for j in range(self._nc):
                s += f'{self._dados[i][j]} '
            s += '\n'
        return s
    
    def __getitem__(self, pos):
        '''Operador []: permite acessar
           um elemento da matriz através de m[i,j].
        '''
        i = pos[0]
        j = pos[1]

        return self._dados[i][j]

    def __setitem__(self, pos, v):
        '''Operador []: permite atribuir um valor
           a um elemento da matriz através de m[i,j].
        '''
        i = pos[0]
        j = pos[1]

        self._dados[i][j] = v
    
    def _checa_dimensoes(self, b, op):
        '''Retorna falso se as dimensões da matriz não são
           compatíveis com as dimensões do parâmetro b, de
           acordo com a op (soma ou multiplicação) desejada.
        '''
        if op == "mul":
            if self._nc == b._nl:
                return True
            else:
                return False
        elif op == "add":
            if self._nl == b._nl and self._nc == b._nc:
                return True
            else:
                return False
        else:
            return False

    def seta_valores(self, valores):
        '''Atribui valores em lista de listas à matriz.'''
        if len(valores) != self._nl or len(valores[0]) != self._nc:
            print('Lista de valores com tamanho incompatível')
        else:
            for i, lin in enumerate(valores):
                for j, v in enumerate(lin):
                    self[i, j] = v

    def __add__(self, b):
        if self._checa_dimensoes(b, "add"):
            Mr = Matriz(self._nl, self._nc)
            
            for i in range(Mr._nl):
                for j in range(Mr._nc):
                    Mr[i, j] = self[i, j] + b[i, j]
            
            return Mr

    def __mul__(self, b):
        '''Operador *'''
        if isinstance(b, (int, float)):
            Mr = self
            for i in range(self._nl):
                for j in range(self._nc):
                    Mr[i, j] *= b
            return Mr
        
        elif self._checa_dimensoes(b, "mul"):
            Mr = Matriz(self._nl, b._nc)

            for i in range(self._nl):
                for j in range(b._nc):
                    for k in range(b._nl):
                        Mr[i, j] += self[i, k] * b[k, j]
            return Mr

    def __eq__(self, b):
        if self._nl != b._nl or self._nc != self._nc:
            return False
        else:
            for i in range(self._nl):
                for j in range(self._nc):
                    if self[i, j] != b[i, j]:
                        return False
            return True

    def __ne__(self, b):
        '''Operador !='''
        if self == b:
            return False
        else:
            return True