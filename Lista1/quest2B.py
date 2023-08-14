def f(x):
    return 2*(x**3)-11.7*(x**2)+17.7*x-5


def g(x):
    return (-2*(x**3)+11.7*(x**2)+5)/(17.7)
# para o intervalo [3,4] temos que abs(g'(x))<1


def mtd_ponto_fixo(xold, n):  # recebe a função, x inicial, max de iteraçoes
    k = 0
    while k < n:
        k += 1
        xnew = g(xold)
        print(f'x[{k}]: {xnew:.6f}, erro: {abs(xnew-xold):.6f}')
        xold = xnew

    return xnew


raiz = mtd_ponto_fixo(3, 3)

print(f'\n A raiz obtida pelo mtd do ponto fixo é aprox {raiz:.6f}')
