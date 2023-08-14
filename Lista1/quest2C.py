def f(x):
    return 2*(x**3)-11.7*(x**2)+17.7*x-5


def g(x):
    return x-f(x)/(6*(x**2)-23.4*x+17.7)

# recebe a função, x inicial, max de iterações


def mtd_newton_raphson(xold, n):
    k = 0
    while k < n:
        k += 1
        xnew = g(xold)
        print(f'x[{k}]: {xnew:.6f}, erro: {abs(xnew-xold):.6f}')
        xold = xnew

    return xnew


raiz = mtd_newton_raphson(3, 3)

print(f'A raiz obtida pelo mtd do ponto fixo é aprox {raiz:.6f}')
