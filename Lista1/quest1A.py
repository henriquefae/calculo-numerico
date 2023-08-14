import matplotlib.pyplot as plt
import numpy as np

q = 20
g = 9.81


def b(x):
    return (q**2)*(3+x)


def a(x):
    return g*((3*x+0.5*(x**2))**3)


def f(x):
    return a(x)-b(x)


def grafico(m, n, p=200):
    x = np.linspace(m, n, p)

    plt.plot(x, a(x), 'r')
    plt.plot(x, b(x), 'g')
    plt.plot(x, f(x), 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


grafico(-10, 10)

print('Pelo método gráfico, a prof crítica é aprox. 1.5116')
