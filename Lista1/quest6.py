import math as mt

Re = 1.1


def f(x, y):
    return 1/mt.sqrt(x) - 4*mt.log10(y*mt.sqrt(x))-0.4


def mtd_bissec(y, xl, xu, erro):
    if f(xl, y)*f(xu, y) > 0:
        print(
            f"O método não converge no intervalo de [{xl}, {xu}] para esse numero de Reynolds")
        return None

    iteracao = 0
    while (abs(xl-xu)) > erro:
        if f(xl, y)*f(xu, y) == 0:
            if f(xl, y) == 0:
                return xl
            else:
                return xu

        t = (xl+xu)/2
        if f(t, y)*f(xu, y) < 0:
            xl = t
        else:
            xu = t
        iteracao += 1
        print(erro/abs(xl-xu))

    return (xl+xu)/2


while Re < 2500 or Re > 1000000:
    Re = float(
        input('Digite o valor para o numero de Reynolds entre 2500 e 1000000: '))


raiz = mtd_bissec(Re, 0.001, 0.01, 0.000005)


if raiz is not None:
    print(f'O fator de atrito é f = {raiz:.6f}, aproximadamente')
