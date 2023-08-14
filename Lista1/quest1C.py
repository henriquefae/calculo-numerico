q = 20
g = 9.81

xl = 0.5
xu = 2.5
erro = 0.001  # menor que 1%
N = 11


def a(x):
    return g*((3*x+0.5*(x**2))**3)


def b(x):
    return (q**2)*(3+x)


def f(x):
    return a(x)-b(x)


def mediaponderada(a, b):
    return (a*abs(f(b))+b*abs(f(a)))/(abs(f(b))+abs(f(a)))


def mtd_falsa_pos(xl, xu, erro, N):
    if f(xl)*f(xu) > 0:
        print(
            f"a função não apresenta raíz no intervalo de [{xl}, {xu}] por esse metodo")
        return None

    iteracao = 0
    while (abs(xl-xu)) > erro and iteracao < N:  # N limita o qnt a função é chamda
        if f(xl)*f(xu) == 0:
            if f(xl) == 0:
                return xl
            else:
                return xu

        t = mediaponderada(xl, xu)
        if f(t)*f(xu) < 0:
            xl = t
        else:
            xu = t
        iteracao += 1

    return mediaponderada(xl, xu)


raiz = mtd_falsa_pos(xl, xu, erro, N)

if raiz is not None:
    print(f'A prof. crítica pelo mtd. da falsa posição é aprox. {raiz:.4f}')

else:
    print('O metodo não convergiu')
