class ponto2D ():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, outroPonto):
        if isinstance(outroPonto, tuple):
            x = self._x + outroPonto[0]
            y = self._y + outroPonto[1]
            result = (x, y)
        elif isinstance(outroPonto, ponto2D):
            x = self._x + outroPonto._x
            y = self._y + outroPonto._y
            result = ponto2D(x, y)
        else:
            result = 'Informe um ponto2D ou uma tuple'

        return result
    
    def __mul__(self, n):
        if isinstance(n, (float, int)):
            x = self._x * n
            y = self._y * n
            return ponto2D(x, y)
        elif isinstance(n, ponto2D):
            pd = self._x * n._x + self._y * n._y
            return pd
        else:
            return 'informe um ponto2D ou um número inteiro'
        
    def __eq__(self, outroPonto):
        if isinstance(outroPonto, tuple):
            if(self._x == outroPonto[0] and self._y == outroPonto[1]):
                return True
            else:
                return False
        elif isinstance(outroPonto, ponto2D):
            if(self._x == outroPonto._x and self._y == outroPonto._y):
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f'ponto2D{self.x, self.y}'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

if __name__ == '__main__':

    p1 = ponto2D(2.0, -2.0)
    p2 = ponto2D(-2.0, 2.0)
    print(p1 + p2) # retorna Ponto2D
    print(p1 + (5.0, 5.0)) # retorna tupla

    p3 = p1 * 4 # multiplica por escalar, retorna Ponto2D
    print(p3)

    print(p1 * p2) # produto interno/escalar, retorna nr. real

    print(p3 == (8.0, -8.0))
    print(p3 == p1)