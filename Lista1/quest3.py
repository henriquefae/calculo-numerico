import math as mt

R = 3


def v(h):
    return mt.pi*(h**2)*(3*R-h)/3


def g(h):
    return h-(v(h)-30)/(mt.pi*h*(2*R-h))


def mtd_newton_raphson(xold, n):
    k = 0
    while k < n:
        k += 1
        xnew = g(xold)
        print(f'h[{k}]: {xnew:.6f}, erro: {abs(xnew-xold):.6f}')
        xold = xnew

    return xnew


raiz = mtd_newton_raphson(R, 3)
