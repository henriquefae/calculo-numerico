import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2*(x**3)-11.7*(x**2)+17.7*x-5


def grafico(m, n, p=200):
    x = np.linspace(m, n, p)

    plt.plot(x, f(x), 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


grafico(-1, 5)

print('Pelo método gráfico, a maior raiz real é aprox. 3.563')
