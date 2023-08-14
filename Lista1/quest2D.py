def f(x):
    return 2*(x**3)-11.7*(x**2)+17.7*x-5


def g(x0, x1):
    return (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))


def mtd_secante(x0, x1, n):
    k = 0
    while k < n:
        k += 1
        x2 = g(x0, x1)
        print(f'x[{k}]: {x2:.6f}, erro: {abs(x2-x1):.6f}')
        x0 = x1
        x1 = x2

    return x2


raiz = mtd_secante(4, 3, 3)

print(f'A raiz obtida pelo mtd do ponto fixo é aprox {raiz:.6f}')
