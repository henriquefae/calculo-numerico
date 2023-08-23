import numpy as np
import math as mt

E = 0.9
r = 0
s = mt.pi-0.1


def f(x, y):
    return y-E*mt.sin(y)-x


def g(x, y):
    return y-f(x, y)/(1-E*mt.cos(y))


def mtd_newton_raphson(x, yold, n):
    k = 0
    while k < n:
        k += 1
        ynew = g(x, yold)
        yold = ynew

    return ynew


def tabela(m, n, p=29):
    x = np.linspace(m, n, p)
    k = 0
    while k < p:
        y = mtd_newton_raphson(x[k], 0, 10)
        print(f"{k+1}) x = {x[k]:.6f} ; y = {y:.6f}")
        k += 1
    print(f"30) x = {mt.pi:.6f} ; y = {mt.pi:.6f}")


tabela(r, s)
