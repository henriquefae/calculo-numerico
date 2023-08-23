k1 = 50000
k2 = 40
m = 90
g = 9.81
h = 0.45


def f(x):
    return 0.4*k2*(pow(x, 2.5))+0.5*k1*(x**2)-m*g*x-m*g*h


def Df(x):
    return k2*pow(x, 1.5)+k1*x-m*g


def z(x):
    return x-f(x)/Df(x)


def mtd_newton_raphson(xold, n):
    k = 0
    while k < n:
        k += 1
        xnew = z(xold)
        print(f'x[{k}]: {xnew:.6f}, erro: {abs(xnew-xold):.6f}')
        xold = xnew

    return xnew


raiz = mtd_newton_raphson(1, 6)
