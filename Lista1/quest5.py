import matplotlib.pyplot as plt
import numpy as np
import math as mt

q = 2e-5
E = 8.85e-12
F = 1.25
a = 0.9
k = q*q/E


def f(x):
    return F-(k*x)/4*mt.pi*pow(x**2+a**2, 1.5)


# mtd grafico para achar boa aproximacao inicial para x


def grafico(m, n, p=600):
    x = np.linspace(m, n, p)

    plt.plot(x, f(x), 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


grafico(0, 5)
# pela analise grafica, temos raiz entre (0.02, 0.08)


def mtd_bissec(xl, xu, erro, N):
    if f(xl)*f(xu) > 0:
        print(
            f"a função não apresenta raíz no intervalo de [{xl}, {xu}] por esse metodo")
        return None

    iteracao = 0
    while (abs(xl-xu)/abs(xu)) > erro and iteracao <= N:  # utilizando erro relativo
        if f(xl)*f(xu) == 0:
            if f(xl) == 0:
                return xl
            else:
                return xu

        t = (xl+xu)/2
        if f(t)*f(xu) < 0:
            xl = t
        else:
            xu = t
        iteracao += 1

    return (xl+xu)/2


raiz = mtd_bissec(0.02, 0.08, 0.0001, 20)

if raiz is not None:
    print(
        f'A distância que satisfaz é aprox. x = {raiz:.6f} metros')
