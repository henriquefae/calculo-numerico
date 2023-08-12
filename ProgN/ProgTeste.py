import matplotlib.pyplot as plt
import numpy as np
import math as mt

q = 20
g = 9.81


def b(x):
    return (q**2)*(3 + x)


def a(x):
    return g*((3*x + 0.5*(x**2))**3)


def f(x):
    return a(x)-b(x)


def grafico(m, n, p=200):
    x = np.linspace(m, n, p)
    y = f(x)
    raizes = []
    raiz = 0

    for i in range(len(x)-1):  # len mede o tamanho do intervalo que x está varrendo
        if (y[i]*y[i+1] < 0):  # aplicação do teorema de Bolzano
            raiz = (x[i]*abs(f(x[i+1])) + x[i+1]*abs(f(x[i]))) / \
                (abs(f(x[i+1])) + abs(f(x[i]))
                 )  # essa operação iterativa da raiz é uma média ponderada
        # append para armazenar a raiz no bloco [] e
        raizes.append(round(raiz, 5))
        # round para arredondar em 5 casas decimais o valor da raiz

        if (y[i] == 0):
            raiz = x[i]
            raizes.append(round(raiz, 5))

    print(raizes)
    plt.plot(x, a(x))
    plt.plot(x, b(x))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


grafico(-10, 10)
