from matriz import Matriz

if __name__ == "__main__":
    a = Matriz(3, 3)
    a[0,2] = 1
    a[1,1] = 1
    a[2,0] = 1
    print('Matriz a:')
    print(a)

    b = Matriz(3, 3)
    b.seta_valores([[1.0, 2.0, 0.0],
                    [2.0, 4.0, 5.0],
                    [3.0, 3.0, 0.0]])
    
    mat_soma = a + b
    print('A + B:')
    print(mat_soma)

    mat_prod = a * b
    print('A * B:')
    print(mat_prod)

    mat_prod = b * 5
    print('B * escalar:')
    print(mat_prod)
    
    print(f'A != B: {a!=b}')
    b.seta_valores([[0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0]])
    print(f'A == B: {a==b}')